# -*- coding: utf-8 -*-
"""Crop-Recommendation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JT2r_ILQYPzxSbGemx_WeWLjjPz4bLrS
"""

from google.colab import drive
drive.mount('/content/gdrive')

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import csv
import numpy as np
import matplotlib as mat
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from __future__ import print_function
from sklearn.metrics import classification_report
from sklearn import metrics
from sklearn import tree
warnings.filterwarnings("ignore")

path= '/content/drive/MyDrive/Crop_recommendation.csv'
df = pd.read_csv(path)

df.info()

df.describe()

df.head()

df.tail()

null_counts = df.isna().sum().sort_values(ascending=False)/len(df)
plt.figure(figsize=(16,8))
plt.xticks(np.arange(len(null_counts))+0.5,null_counts.index,rotation='vertical')
plt.ylabel('fraction of rows with missing data')
plt.bar(np.arange(len(null_counts)),null_counts)

df.size

df.columns

df['label'].value_counts()

sns.heatmap(df.corr(), annot=True)

features = df[['N', 'P','K','temperature', 'humidity', 'ph', 'rainfall']]
target = df['label']
labels = df['label']

acc = []
model = []

# Splitting into train and test data

from sklearn.model_selection import train_test_split
Xtrain, Xtest, Ytrain, Ytest = train_test_split(features,target,test_size = 0.2,random_state =2)

from sklearn.linear_model import LogisticRegression

LogReg = LogisticRegression(random_state=2)

LogReg.fit(Xtrain,Ytrain)

predicted_values = LogReg.predict(Xtest)

x = metrics.accuracy_score(Ytest, predicted_values)
acc.append(x)
model.append('Logistic Regression')
print("Logistic Regression's Accuracy is: ", x)

print(classification_report(Ytest,predicted_values))

import pickle
from sklearn.linear_model import LogisticRegression

LogReg = LogisticRegression(random_state=2)

LogReg.fit(Xtrain,Ytrain)

predicted_values = LogReg.predict(Xtest)

accuracy = metrics.accuracy_score(Ytest, predicted_values)

print("Logistic Regression's Accuracy using Bottom-up approach: ", accuracy)


# Dump the trained Naive Bayes classifier with Pickle
LR_pkl_filename = 'LogisticRegression.pkl'

# Open the file to save as pkl file
LR_Model_pkl = open('./model.pkl', 'wb')

pickle.dump(LogReg, LR_Model_pkl)

# Close the pickle instances
LR_Model_pkl.close()