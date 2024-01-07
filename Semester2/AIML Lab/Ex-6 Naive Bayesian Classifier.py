import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score

df = pd.read_csv('Datasets/diabetes.csv')

df.isna().sum()

# sns.heatmap(df.corr(method='kendall'), annot=True)
# plt.show()

X = df.drop(columns=['Outcome'])
y = df['Outcome']

xtr, xts, ytr, yts = train_test_split(X, y, train_size=.7, random_state=123)

sc = StandardScaler()
sc_obj = sc.fit(xtr)

sctr, scts = sc_obj.transform(xtr), sc_obj.transform(xts)

clsfr = GaussianNB()
clsfr.fit(sctr, ytr)

y_prd_ts = clsfr.predict(scts)
y_prd_tr = clsfr.predict(sctr)

conf_matrix_ts = confusion_matrix(yts, y_prd_ts)
print("Confusion Matrix for Test Data:")
print(conf_matrix_ts)

acc_score_ts = accuracy_score(yts, y_prd_ts)
print(f"Accuracy Score for Test Data: {acc_score_ts}")

acc_score_tr = accuracy_score(ytr, y_prd_tr)
print(f"Accuracy Score for Training Data: {acc_score_tr}")

# Plotting the graph
plt.figure(figsize=(10, 6))
plt.scatter(df['DiabetesPedigreeFunction'], df['Age'], c=df['Outcome'], cmap='viridis')
plt.colorbar(label='Outcome', ticks=[0, 1])
plt.xlabel('DiabetesPedigreeFunction')
plt.ylabel('Age')
plt.title('Diabetes vs Age with Outcome')
plt.show()
