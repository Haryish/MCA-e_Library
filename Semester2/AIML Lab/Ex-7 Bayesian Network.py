import pandas as pd
import numpy as np
import csv

from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.models import BayesianNetwork
from pgmpy.inference import VariableElimination

heart_df = pd.read_csv('Datasets/heart.csv')
heart_df = heart_df.replace('?',np.nan)

heart_df.columns

model = BayesianNetwork([('age','target'),('sex','target'),('exang','target'),('cp','target'),
                ('target','restecg'),('target','chol')])

model.fit(heart_df,estimator = MaximumLikelihoodEstimator)

heart_disease_infer = VariableElimination(model)

print('\n 1. Probability of Heart Disease given evidence = restecg')
q1 = heart_disease_infer.query(variables = ['target'],evidence={'restecg':1})
print(q1)

print('\n 2. Probability of Heart Disease given evidence = cp')
q2 = heart_disease_infer.query(variables = ['target'],evidence={'cp':2})
print(q2)

for c in heart_df:
    print(c)
    print(heart_df[c].value_counts())
