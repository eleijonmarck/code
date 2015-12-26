library(RODBC)
library(ggplot2)
library(dplyr)
library(reshape2)

dbhandle <- odbcDriverConnect('driver={SQL Server};server=(local);database=SN;trusted_connection=true')

data.raw <- sqlQuery(dbhandle, 'select * from vwMedlemsbolag')
data.raw$Uttrade <- factor(!is.na(data.raw$Uttradesdatum))
levels(data.raw$Uttrade) <- c("Kvar", "Lämnade")

plot(density(filter(data.raw, BolagsAlder >= 0)$BolagsAlder), ylab = "", xlab ="Ålder", main = "Bolagsålder bef medlemmar")
plot(density(filter(data.raw, BolagsAlderVidIntrade >= 0)$BolagsAlderVidIntrade), ylab = "", xlab ="Ålder", main = "Bolagsålder vid inträde")
plot(density(filter(data.raw, BolagsAlderVidUttrade >= 0)$BolagsAlderVidUttrade), ylab = "", xlab ="Ålder", main = "Bolagsålder vid utträde")

q <- melt(data.raw[c("BolagsAlder", "BolagsAlderVidIntrade", "BolagsAlderVidUttrade")])

ggplot(q, aes(x=value)) + 
  geom_density(aes(group=variable, colour=variable)) + 
  ylab("Andel") +
  xlab("Ålder") +
  theme(
    axis.text.x = element_text(size=18), 
    axis.title.x = element_text(size=18), 
    axis.text.y = element_text(size=18), 
    axis.title.y = element_text(size=18), 
    legend.text=element_text(size=18))  


sniFrequencyBefintliga <- as.data.frame(tablefilter(data.raw, is.na(Uttradesdatum))$SNIKodUtanText)
sniFrequencyBefintliga$Freq <- sniFrequencyBefintliga$Freq / sum(sniFrequencyBefintliga$Freq)
sniFrequencyUttradande <- as.data.frame(table(filter(data.raw, !is.na(Uttradesdatum))$SNIKodUtanText))
sniFrequencyUttradande$Freq <- sniFrequencyUttradande$Freq / sum(sniFrequencyUttradande$Freq)

topSNI <- head(sniFrequency[order(sniFrequencyBefintliga$Freq, decreasing = T),], n = 5)$Var1

sniMerge <- data.frame(SNI = factor(topSNI))

sniMerge <- inner_join(sniMerge, sniFrequencyBefintliga, by = c("SNI" = "Var1"))
sniMerge <- inner_join(sniMerge, sniFrequencyUttradande, by = c("SNI" = "Var1"))
sniMerge <- rename(sniMerge, Befintliga = Freq.x, Utträdande = Freq.y)
sniMergeMelt <- melt(sniMerge, id=c("SNI"))

ggplot(sniMergeMelt, aes(x=SNI, y=value, fill=variable)) + 
  geom_bar(stat="identity", position="dodge") +
  ylab("Andel") +
  xlab("SNI-kod") +
  theme(
    axis.text.x = element_text(size=18), 
    axis.title.x = element_text(size=18), 
    axis.text.y = element_text(size=18), 
    axis.title.y = element_text(size=18), 
    legend.text=element_text(size=18))  


# BeslutstrÃ¤d
require(rpart)
require(rpart.plot)
require(rattle)

data.pred <- data.raw
data.pred$Intradesdatum <- NULL
data.pred$Uttradesdatum <- NULL
data.pred$`Registreringsdatum:` <- NULL
data.pred$Kommunsate <- NULL
data.pred$SNIKod <- NULL
data.pred$Latitud <- NULL
data.pred$Longitud <- NULL
data.pred$Namn <- NULL
data.pred$Orgnummer <- NULL
data.pred$Ort <- NULL
data.pred$Gatuadress <- NULL
data.pred$Postnummer <- NULL
data.pred$BolagsAlderVidIntrade <- NULL
data.pred$BolagsAlderVidUttrade <- NULL

data.pred$SNIKodUtanText <- NULL

plot.tree <- function(tree) {
  prp(tree, type=3,extra=109, clip.right.labs = F, faclen=100)
}

tree <- rpart(Uttrade ~., data = data.pred, control = rpart.control())
plot.tree(tree)

# Prediktion
library(caret)


data.pred <- data.raw
data.pred$Intradesdatum <- NULL
data.pred$Uttradesdatum <- NULL
data.pred$`Registreringsdatum:` <- NULL
data.pred$Kommunsate <- NULL
data.pred$SNIKod <- NULL
data.pred$Latitud <- NULL
data.pred$Longitud <- NULL
data.pred$Namn <- NULL
data.pred$Orgnummer <- NULL
data.pred$Ort <- NULL
data.pred$Gatuadress <- NULL
data.pred$Postnummer <- NULL
data.pred$BolagsAlderVidIntrade <- NULL
data.pred$BolagsAlderVidUttrade <- NULL

q <- na.omit(data.pred)

ix <- sample(nrow(q), nrow(q) * 0.75)

train <- q[ix,]
test <- q[-ix,]

fit <- train(Uttrade ~ ., data = train, preProcess = c("center", "scale"), method="rf")

predicted_result <- predict(fit, test)
confusionMatrix(predicted_result, reference = test$Uttrade)

variable.importance <- varImp(fit)
plot(variable.importance)

#
# Deep learning
#
library(h2o)

localH2O = h2o.init(nthreads = -1)

# Set up train and test data
s <- sample(1:nrow(q), nrow(q) * 0.7)

train <- q[s,]
test <- q[-s,]

train_h2o <- as.h2o(localH2O, train)
test_h2o <- as.h2o(localH2O, test)


#
#
#

models <- c()

# Generate grid frame
variations.count <- 10
variations.frame <- data.frame(
  activation = replicate(variations.count, c("TanhWithDropout", "RectifierWithDropout")[sample(1:2,1)]),
  # Only try Rectifier with dropout since that seems to work best
  #activation = "RectifierWithDropout",
  numlayers = replicate(variations.count, sample(2:4,1)),
  l1 = replicate(variations.count, runif(1, 0, 1e-3)),
  l2 = replicate(variations.count, runif(1, 0, 1e-3)),
  input_dropout <- replicate(variations.count, runif(1, 0, 0.5))
)

variations.frame$dropout <- lapply(variations.frame$numlayers, function(numlayers) c(runif(numlayers, 0, 0.6)))
variations.frame$hidden <- lapply(variations.frame$numlayers, function(numlayers) c(sample(5:50,numlayers,T)))

# Perform grid search 
for (i in 1:nrow(variations.frame)) {
  
  row <- variations.frame[i,]
  
  dlmodel <- h2o.deeplearning(
    x = c(1:(ncol(data.tpset)-1)), 
    y = ncol(data.tpset), 
    training_frame = train_h2o, 
    validation_frame = test_h2o, 
    epochs = row$numlayers * 500,
    activation = as.character(row$activation), 
    hidden = row$hidden[[1]], 
    l1 = row$l1, 
    l2 = row$l2,
    input_dropout_ratio = row$input_dropout, 
    hidden_dropout_ratios = row$dropout[[1]])
  
  print(c(dlmodel@model$validation_metrics@metrics$MSE, dlmodel@model$validation_metrics@metrics$r2,  dlmodel@model$validation_metrics@metrics$AUC))
  
  models <- c(models, dlmodel)
}

# get model stats
modelstats <- sapply(models, function(x) c(validation_r2=x@model$validation_metrics@metrics$r2, 
                                           test_r2=x@model$training_metrics@metrics$r2, 
                                           l1=x@parameters$l1, 
                                           l2=x@allparameters$l2, 
                                           layers=length(x@parameters$hidden),
                                           model_id=x@model_id))

modelstats <- data.frame(t(modelstats))

modelstats[,1:5] <- lapply(modelstats[,1:5], function(x) as.numeric(as.character(x)))

modelstats <- arrange(modelstats, desc(validation_r2))

# select best model
best_model <- h2o.getModel(modelstats$model_id[1],localH2O)

# Train the best model some more
#row <- variations.frame[best_model_index,]
#best_model <- models[[best_model_index]]

best_model


