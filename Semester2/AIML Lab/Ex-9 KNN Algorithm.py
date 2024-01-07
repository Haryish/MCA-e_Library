import numpy as np
import pandas as pd
from sklearn import datasets
iris = datasets.load_iris()
     

x,y = pd.DataFrame(iris['data'],columns=iris['feature_names']),pd.DataFrame(iris['target'],columns=['target'])
y
     

dataset = x
dataset['target'] = y
import matplotlib.pyplot as plt
import seaborn as sns

from pandas.plotting import parallel_coordinates
plt.figure(figsize=(15,10))
parallel_coordinates(dataset, "target")
plt.title('Parallel Coordinates Plot', fontsize=20, fontweight='bold')
plt.xlabel('Features', fontsize=15)
plt.ylabel('Features values', fontsize=15)
plt.legend(loc=1, prop={'size': 15}, frameon=True,shadow=True, facecolor="white", edgecolor="black")
plt.show()
     

from sklearn.model_selection import train_test_split
xtr, xts, ytr, yts = train_test_split(x, y, test_size = 0.2, random_state = 0)
from pandas.plotting import andrews_curves
plt.figure(figsize=(15,10))
andrews_curves(dataset, "target")
plt.title('Andrews Curves Plot', fontsize=20, fontweight='bold')
plt.legend(loc=1, prop={'size': 15}, frameon=True,shadow=True, facecolor="white", edgecolor="black")
plt.show()
     

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import cross_val_score


classifier = KNeighborsClassifier(n_neighbors=3)


classifier.fit(xtr, ytr)


y_pred = classifier.predict(xts)
cm = confusion_matrix(yts, y_pred)
cm
     

# creating list of K for KNN
k_list = list(range(1,50,2))
# creating list of cv scores
cv_scores = []

# perform 10-fold cross validation
for k in k_list:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, xtr, ytr, cv=10, scoring='accuracy')
    cv_scores.append(scores.mean())
     

xtr
     

ytr.columns
     

cv_scores
     

MSE = [1 - x for x in cv_scores]

plt.figure()
plt.figure(figsize=(15,10))
plt.title('The optimal number of neighbors', fontsize=20, fontweight='bold')
plt.xlabel('Number of Neighbors K', fontsize=15)
plt.ylabel('Misclassification Error', fontsize=15)
sns.set_style("whitegrid")
plt.plot(k_list, MSE)

plt.show()
