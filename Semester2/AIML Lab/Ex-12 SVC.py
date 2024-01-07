import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('Datasets/breast_cancer.csv')

target = df['diagnosis']

s = set()
for val in target:
    s.add(val)
s = list(s)

x = df['radius_mean']
y = df['concavity_mean']
open_x = x[:50]
open_y = y[:50]
high_x = x[50:100]
high_y = y[50:100]
plt.figure(figsize=(10,8))
plt.scatter(open_x,open_y,marker='+',color='green')
plt.scatter(high_x,high_y,marker='_',color='red')
plt.show()
