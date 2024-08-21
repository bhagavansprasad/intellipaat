import pandas as pd
import numpy as np

#machine learning related packages
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

def print_full(d):
    d.index.name = 'MyIdx'
    d = d.sort_values(by = ['MyIdx'], ascending = [True])
    pd.set_option('display.max_rows', len(d))
    print(d)
    pd.reset_option('display.max_rows')
    
def dump_data(objname, d):
    # print(d.info())
    # d.index.name = 'MyIdx'
    # d = d.sort_values(by = ['MyIdx'], ascending = [True])
    print(f"{objname} : {d.shape}")
    
    try:
        print(d.head())
    except:
        print
        print(d)
    # print(d)
    # print_full(d)
    print()

def best_fit_line():
    # cleanup data
    data = pd.read_csv('Boston.csv')
    print(data.head())
    print(data.info())
    print(data.isnull())
    print(data.isnull().sum())
    print(data.duplicated().sum())
    data.drop_duplicates(inplace = True)
    
    X = data.drop(columns='medv')
    print(X.info())
    print(X.head())

    y = data['medv']
    print(y.info())
    print(y.head())
    
    """### **Split our data into training and testing sets**"""

    dump_data("X...", X)
    #   X = all input columns
    #   y = ouput columns
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
    
    dump_data("X_train", X_train)
    dump_data("X_test...", X_test)
    dump_data("y_train...", y_train)
    dump_data("y_test...", y_test)

    lin_reg = LinearRegression()
    lin_reg.fit(X_train, y_train)   #learning process starts here

    dump_data("coef...", lin_reg.coef_)   #beta1 to beta13
    dump_data("intercept...", lin_reg.intercept_)  #beta0

    y_pred = lin_reg.predict(X_test)
    
    dump_data("y_pred...", y_pred)
    dump_data("y_test...", y_test)
    dump_data("r2_score...", r2_score(y_test, y_pred))

    from statsmodels.stats.outliers_influence import variance_inflation_factor

    vif = pd.DataFrame()
    vif['Features'] = X_train.columns
    vif['VIF'] = [variance_inflation_factor(X_train.values, i) for i in range(X_train.shape[1])]
    vif['VIF'] = round(vif['VIF'], 2)
    print(vif)

    dump_data("X_train", X_train)
    X_train.drop(columns=['ptratio'])


def main():
    best_fit_line()

# Can we categorize these steps as normalization?

# Normalizing data before applying ML algos
    #1. Datatypes - 
        # ML algos does not work properly with strings
        # Int datatype is always better
    #2. Replace null with appropriate values
    #3. Remove duplicates
# Identify input and output colums
#   X = all input columns
#   y = ouput columns

if (__name__ == '__main__'):
    main()

