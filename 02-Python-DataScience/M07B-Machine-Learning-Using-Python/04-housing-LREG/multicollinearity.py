import pandas as pd
import numpy as np

# TODO: FAQs to answer
# What columns are considered as training data
#   Except medv, every other column is considered
# What columns are considered as test data?
# How to print only Test data Actual-value and Predicted-value?
# How to caliculated the error marning for each row of test data?
# What is the total error margin for all test data?
# What is R2score, how is it calculated?
# Is Correlation and variance_inflation_factor is on and the same?
# What is the difference between X_train and y_train?
# Why shape is not giving number of columns y_train, y_test and y_pred?
# Is variance_inflation_factor can be done with bool column types?
#   I am getting error "TypeError: ufunc 'isfinite' not supported for the input types"

#machine learning related packages
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
from statsmodels.stats.outliers_influence import variance_inflation_factor
from tabulate import tabulate
import matplotlib.pyplot as plt
import seaborn as sns

def calc_variance_inflation_factor(X_train):
    vif = pd.DataFrame()
    vif['Features'] = X_train.columns
    
    vif['VIF'] = [variance_inflation_factor(X_train.values, i) for i in range(X_train.shape[1])]
    for i in range(X_train.shape[1]):
        t = variance_inflation_factor(X_train.values, i)
        
    vif['VIF'] = round(vif['VIF'], 2)
    
    return vif

def dump_data(objname, d):
    try:
        print(f"shape :{d.shape}")
        print(f"info  :{d.info()}")
    except:
        pass
    
    # print(d)
    print()
    
def get_r2score_vif(data, output_col):
    X = data.drop(columns=output_col)
    y = data[output_col]
    
    #   X = all input columns
    #   y = ouput columns
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
    
    lin_reg = LinearRegression()
    lin_reg.fit(X_train, y_train)   #learning process starts here

   
    y_pred = lin_reg.predict(X_test)
    r2score = r2_score(y_test, y_pred)

    # dump_data("X_train", X_train) 
    # dump_data("X_test ", X_test) 
    # dump_data("y_train", y_train) 
    # dump_data("y_test ", y_test) 
    # dump_data("y_pred ", y_pred) 

    vif = calc_variance_inflation_factor(X_train)

    return r2score, vif

def fill_vfs_results(colnames, nfeatures, viflist):
    tdict = {}
    
    for cn in colnames:
        tdict[cn] = viflist[nfeatures[cn]] if cn in nfeatures else 0
    
    return tdict

def my_sort_fun(setvalue):
    return float(setvalue[1])
    
def get_max_vif(td):
    tlist = list(td.items())
    tlist = sorted(tlist, reverse=True, key=my_sort_fun)
    return tlist[0][0], tlist[0][1]

def display_fine_tuned_results(vifresults):
    header = list(vifresults[0].keys())
    header.insert(0, "Row")
    rows = []
    for i, x in enumerate(vifresults, 1):
        t = list(x.values())
        t.insert(0, i)
        rows.append(t)
        
    print()
    print(tabulate(rows, header))
    print()
    
def multicollinearity(df, output_col):
    colnames = df.columns.to_list()
    colnames.remove(output_col)
    colnames.append('R2Score')
    
    vifresults = []

    for i in range(0, len(colnames)):
        r2score, vif = get_r2score_vif(df, output_col)

        dlist = vif.to_dict('dict')
        features = dlist['Features']
        features[len(features)] = "R2Score"

        viflist  = dlist['VIF']
        viflist[len(viflist)] = float(r2score)
        
        nfeatures = dict((v,k) for k,v in features.items())
        
        # print(f"features   :{features}")
        # print(f"nfeatures  :{nfeatures}")
        # print(f"viflist    :{viflist}")

        td = fill_vfs_results(colnames, nfeatures, viflist)
        vifresults.append(td)
        
        colname, maxvif = get_max_vif(td)

        if (maxvif <= 5):
            break
        
        df.drop(columns=colname, inplace=True)

    display_fine_tuned_results(vifresults)
    return df


def apply_multicollinearity(df, output_col):
    return multicollinearity(df, output_col)

