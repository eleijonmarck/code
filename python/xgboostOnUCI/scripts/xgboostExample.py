#!/bin/python3
import numpy
import xgboost
from sklearn import cross_validation
from sklearn.metrics import accuracy_score

# load data
dataset = numpy.loadtxt('../data/pima-indians-diabetes.csv',delimiter=",")

# split data into X and y
X = dataset[:,0:8]
y = dataset[:,8]

# split data into train and test sets

seed = 7
test_size = 0.33
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y,
        test_size=test_size, random_state=seed)

model = xgboost.XGBClassifier()
model.fit(X_train, y_train)

print(model)


# make predictions for test data
y_pred = model.predict(X_test)
'''
By default, the predictions made by XGBoost are probabilities. Because
this is a binary classification problem, each prediction is the
probability of the input pattern belonging to the first class. We can
easily convert them to binary class values by rounding them to 0 or 1.
'''
predictions = [round(value) for value in y_pred]

'''
Now that we have used the fit model to make predictions on new data, we
can evaluate the performance of the predictions by comparing them to the
expected values. For this we will use the built in accuracy_score()
function in scikit-learn.
'''

# evaluate predictions
accuracy = accuracy_score(y_test, predictions)
print("Accuracy : %.2f%%" % (accuracy * 100.0))
