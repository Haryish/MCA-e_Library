import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import seaborn as sns

df = pd.read_csv('Datasets/diabetes.csv')

x = df.iloc[:,:-1]
y = df.iloc[:,-1]

xtr,xts,ytr,yts = train_test_split(x,y,train_size=0.7)

sc = StandardScaler()
sc.fit(xtr)
sctr = sc.transform(xtr)
scts = sc.transform(xts)

model = LogisticRegression()
model.fit(sctr,ytr)

y_prd_ts = model.predict(scts)
y_prd_tr = model.predict(sctr)

accuracy_score(yts,y_prd_ts)

accuracy_score(ytr,y_prd_tr)

# Assuming yts, y_prd_ts are binary labels (0 or 1)
cm = confusion_matrix(yts, y_prd_ts)

# Plot the confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False)
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("True")
plt.show()
