# Import libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
# from sklearn.svm import SVC
from sklearn.externals import joblib
from sklearn import datasets

# Get the dataset
dataset = datasets.load_iris()

# Split the dataset into features and labels
X = dataset.data
y = dataset.target

# Split the dataset into training (80%) and testing (20%) data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0, shuffle = True)

### Build the classifier and make prediction
### DecisionTree
classifier = DecisionTreeClassifier()
classifier.fit(X_train, y_train)
prediction = classifier.predict(X_test)

### SVM, Support Vector Machine
# classifier = SVC(C=1.0, kernel="rbf", probability=True)
# classifier.fit(X_train, y_train)
# prediction = classifier.predict(X_test)

# Print the confusion matrix
print("Confusion Matrix:")
print(metrics.confusion_matrix(y_test, prediction))
print(metrics.classification_report(y_test, prediction))

# Save the model to disk
joblib.dump(classifier, 'classifier.joblib')