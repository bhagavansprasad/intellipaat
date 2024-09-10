# https://docs.google.com/forms/d/e/1FAIpQLScq-O4sJFPGHuuwR-_DcFIIC-LAcQ78ArUfwfLko2IpaEmONA/viewform
# https://www.kaggle.com/datasets/tawfikelmetwally/census-income-dataset

#  #   Column          Non-Null Count  Dtype
# ---  ------          --------------  -----
#  0   age             32561 non-null  int64
#  1   workclass       32561 non-null  object
#  2   fnlwgt          32561 non-null  int64
#  3   education       32561 non-null  object
#  4   education-num   32561 non-null  int64
#  5   marital-status  32561 non-null  object
#  6   occupation      32561 non-null  object
#  7   relationship    32561 non-null  object
#  8   race            32561 non-null  object
#  9   sex             32561 non-null  object
#  10  capital-gain    32561 non-null  int64
#  11  capital-loss    32561 non-null  int64
#  12  hours-per-week  32561 non-null  int64
#  13  native-country  32561 non-null  object
#  14  annual_income   32561 non-null  object
# dtypes: int64(6), object(9)
# memory usage: 3.7+ MB
# None


import pandas as pd
import math
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split #spliting the data into train and test
from sklearn import tree #loading the package
from sklearn.metrics import accuracy_score,confusion_matrix #evalution matrix
from sklearn.metrics import *
from autoviz.AutoViz_Class import AutoViz_Class
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder #encoding
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,accuracy_score

def get_dataset():
    return DATA_SET

def is_data_loaded(df):
    print(f"Top rows...")
    print(df.head())
    print()

def data_undertand_structure(df):
    print(f"Shape...")
    print(df.shape)
    print()
    
    print(f"Column Names...")
    collist = df.columns.to_list()
    print(f"{collist}")
    
    print(f"Information of data...")
    print(df.info())
    print()

def print_unique_values_by_feature(df, features):
    for attribute in features:
        print(f"feature :{attribute}..")
        print(len(df[attribute].unique()), df[attribute].unique())
        print()

# def visualization_box_plot(df, pair):
#     # plt.figure(figsize=(5, 5))
#     plt.figure()
#     # plt.subplot(2,3,1)
#     sns.boxplot(x = pair[0], y = pair[1], data = df)
#     plt.show()

# def data_visualization(df):
#     features_list = ["price", "area", "bedrooms", "bathrooms", "stories", "parking"]
#     features_list = []
#     visualize_numerical_features(df, features_list)
    
#     features_list = ["area", "bedrooms", "price"]
#     features_list = []
#     visualize_pairplot(df, features_list)

#     features_list = ["area", "bedrooms", "price"]
#     features_list = []
#     visualize_correlation_matrix(df, features_list)
    
#     features_pairs = [
#         ['mainroad', 'price'],
#         ['guestroom', 'price'],
#         ['basement', 'price'],
#         ['hotwaterheating', 'price'],
#         ['airconditioning', 'price'],
#         ['furnishingstatus','price'],
#     ]
#     features_pairs = []
#     for pair in features_pairs:
#         visualization_box_plot(df, pair)

# def visualize_correlation_matrix(df, features_list):
#     if not len(features_list):
#         return 

#     correlation_matrix = df.corr(features_list)
#     fig, ax = plt.subplots(figsize=(8, 6))

#     sns.heatmap(correlation_matrix, annot=True, cmap='YlOrRd', ax=ax)

#     ax.set_title('Correlation Matrix')
#     ax.set_xlabel('Numerical Features')
#     ax.set_ylabel('Numerical Features')

#     plt.tight_layout()
#     plt.show()

# Defining a Function to Convert Objects to Int
def object_to_int(dataframe_series):# function
    if dataframe_series.dtype=='object': #condition
        dataframe_series = LabelEncoder().fit_transform(dataframe_series) #label enconder to my dataset
    return dataframe_series

def apply_logistic_regression(df):
    df2 = df
    df = df.apply(lambda x: object_to_int(x))

    X = df.drop(columns = [OUTPUT_COLUMN])
    y = df[OUTPUT_COLUMN].values
    
    x_train,x_test,y_train,y_test=train_test_split(X, y, train_size=0.8)    
    log_model=LogisticRegression()
    log_model.fit(x_train,y_train)
    
    y_pred=log_model.predict(x_test)
    confusion_matrics=confusion_matrix(y_test,y_pred)
    # print(confusion_matrics)
    
    score = accuracy_score(y_test, y_pred)
    score = round(score*100, 4)
    print(f"Logistic Regression score :{score}")

def apply_decision_tree(df):
    df2 = df
    df = df.apply(lambda x: object_to_int(x))

    X = df.drop(columns = [OUTPUT_COLUMN])
    y = df[OUTPUT_COLUMN].values
    
    x_train,x_test,y_train,y_test=train_test_split(X, y, train_size=0.8)    

    clf = tree.DecisionTreeClassifier()
    clf.fit(x_train,y_train)  #to fit the model
    y_train_pred = clf.predict(x_train)#this is only to check the train accuracy
    y_test_pred = clf.predict(x_test)#this is only to check the test accuracy

    # accuracy_score(y_train_pred,y_train)
    score = accuracy_score(y_test_pred,y_test)
    score = round(score*100, 4)
    
    print(f"Decision Tree score       :{score}")
    
def random_forest(df):
    df2 = df
    df = df.apply(lambda x: object_to_int(x))

    X = df.drop(columns = [OUTPUT_COLUMN])
    y = df[OUTPUT_COLUMN].values
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model_rf = RandomForestClassifier(
        n_estimators=1000,
        random_state=65,
        max_leaf_nodes=7 # use the squaure root of your parameter
    )

    model_rf.fit(X_train, y_train)

    prediction_test = model_rf.predict(X_test)

    score = accuracy_score(y_test, prediction_test)
    score = round(score*100, 4)
    print(f"Random Forest score       :{score}")
    
    # print(classification_report(y_test, prediction_test))

DATA_SET =  "census-income.csv"
OUTPUT_COLUMN = "annual_income"
OUTPUT_VALUES = [1, 0]
FEATURES = ["workclass", "education", "education-num", "marital-status", "occupation", "relationship", "race", "sex", "annual_income"]
    
def main():
    data_set = get_dataset()
    df = pd.read_csv(data_set)

    # eda
    is_data_loaded(df)
    data_undertand_structure(df)
    # print_unique_values_by_feature(df, FEATURES)
    
    # print(df.isnull())
    # print(df.isnull().sum())
    # print(df.duplicated().sum())
    df.drop_duplicates(inplace = True)
    print(df.shape)

    df.loc[df.annual_income == "<=50K", 'annual_income'] = 0
    df.loc[df.annual_income == ">50K", 'annual_income'] = 1
    df['annual_income'] = pd.to_numeric(df['annual_income'])

    df.loc[df.sex == "Female", 'sex'] = 0
    df.loc[df.sex == "Male", 'sex'] = 1
    df['sex'] = pd.to_numeric(df['sex'])
                        
    df.drop('education', axis=1, inplace=True)

    FEATURES.remove('education')
    print_unique_values_by_feature(df, FEATURES)
    data_undertand_structure(df)
    
    numaric_features = ["age","education-num", "sex", "capital-gain", "capital-loss", "hours-per-week", "annual_income"]
    # visualize_correlation_matrix(df, numaric_features)

    AV = AutoViz_Class()
    report = AV.AutoViz(df)
    print(report)

    print("=" * 75)
    apply_logistic_regression(df)
    apply_decision_tree(df)
    random_forest(df)
    print("=" * 75)
    return
    

if (__name__ == '__main__'):
    main()
