# -*- coding: utf-8 -*-
"""Linear Regression Practical 20 Aug.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1727bDNfIRKzQ-5K9HCDSROeTGHheDS9Y

### For colab users to upload the files
"""

# from google.colab import files
# uploaded = files.upload()

"""### **Import the required packages**"""

import pandas as pd
import numpy as np

#machine learning related packages
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

"""### **Reading the data**"""

data = pd.read_csv('Boston.csv')

print(data.head())
print(data.shape)
print(data.dtypes)  #to check the datatype of each column

"""**Note:** Machine Learning Algorithms don't work well with text data so if our data has text values, we need to encode(convert from text to numbers) it before using it with machine learning algorithms."""

#check for the missing values
print(data.isnull().sum())

#check for duplicates
print(data.duplicated().sum())  #check how many rows are duplicate

#print the rows which are duplicate
print(data[data.duplicated()])

#drop or remove the duplicate rows
print(data.drop_duplicates(inplace = True))

"""### **Machine Learning Process**"""

#Identify input and output columns
X = data.drop(columns = 'medv')   #all the input cols
y = data['medv']   #the output col

"""### **Split our data into training and testing sets**"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

"""### **Apply Linear Regression**"""

lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)   #learning process starts here

print(lin_reg.coef_)   #beta1 to beta13

print(lin_reg.intercept_)  #beta0

y_pred = lin_reg.predict(X_test)

print(y_pred)
print(y_test)
print(r2_score(y_test, y_pred))

"""### Performance metric to be used for regression data.

- Mean Squared error(MSE).
- Root Mean Squared Error(RMSE).
- R- Squared(R2_score).
"""

mse = mean_squared_error(y_test, y_pred)
print(mse)

rmse = np.sqrt(mse)
print(rmse)

"""#### The Model is making an average error of 4.46 while predicting each value."""

from statsmodels.stats.outliers_influence import variance_inflation_factor

vif = pd.DataFrame()
vif['Features'] = X_train.columns
vif['VIF'] = [variance_inflation_factor(X_train.values, i) for i in range(X_train.shape[1])]
vif['VIF'] = round(vif['VIF'], 2)
print(vif)

# X_train.drop('ptratio')