require(xlsx)
q <- read.xlsx("beerdata.xlsx", sheetIndex = 1, startRow = 3)

q$Date <- NULL
q$Voter <- NULL
q$Session <- NULL

colnames(q) <- c("Age", "City", "Gender", "Prog", "Beer")
levels(q$Beer) <- c("Ale", "Lager", "Stout", "Veteöl")

xtabs(~Beer+Gender, q)
xtabs(~Beer+City, q)

# Beslutsträd
require(rpart)
require(rpart.plot)

tree <- rpart(Beer ~., data = q, control = rpart.control(minsplit = 5))
plot.tree(tree)

# Neuralt nätverk
require(nnet)
require(caret)

ix <- sample(nrow(q), nrow(q) * 0.8)

train <- q[ix,]
test <- q[-ix,]

modelFit <- nnet(Beer ~ ., data = train, size=5, decay=0.001, trace=F)
modelFit
plot.nnet(modelFit)

predicted_result <- predict(modelFit, test, type="class")
confusionMatrix(predicted_result, reference = test$Beer)
