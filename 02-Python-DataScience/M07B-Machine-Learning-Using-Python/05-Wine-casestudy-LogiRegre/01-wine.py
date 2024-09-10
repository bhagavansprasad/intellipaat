import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# from multicollinearity import apply_multicollinearity

# RangeIndex: 6497 entries, 0 to 6496
# Data columns (total 13 columns):
#  #   Column                Non-Null Count  Dtype
# ---  ------                --------------  -----
#  0   fixed acidity         6497 non-null   float64
#  1   volatile acidity      6497 non-null   float64
#  2   citric acid           6497 non-null   float64
#  3   residual sugar        6497 non-null   float64
#  4   chlorides             6497 non-null   float64
#  5   free sulfur dioxide   6497 non-null   float64
#  6   total sulfur dioxide  6497 non-null   float64
#  7   density               6497 non-null   float64
#  8   pH                    6497 non-null   float64
#  9   sulphates             6497 non-null   float64
#  10  alcohol               6497 non-null   float64
#  11  quality               6497 non-null   object
#  12  type                  6497 non-null   object
# dtypes: float64(11), object(2)

DATA_SET =  "wine_fraud.csv"
OUTPUT_COLUMN = "quality"

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
    print(f"Column Names :{collist}\n")
    
    print(f"Information of data...")
    print(df.info())
    print()
    
def check_missing_values(df):
    print(f"Understanding Null values...")
    print(df.isnull())
    print(df.isnull().sum())
    print()

def get_numerical_stats(df):
    print(f"Stats of Numerical data...")
    print(df.describe())
    print()

def data_quality(df):
    
    print(f"Unique values :{df.nunique()}")
    print(f"Unique count Quality : {df['quality'].nunique()}")
    print(f"Unique Quality values: {df['quality'].unique()}")
    print(f"Value count Quality values:\n {df['quality'].value_counts()}")

def get_categorical_frequencies(df):
    combined_results = pd.DataFrame(columns=['Column', 'Value', 'Frequency'])
    
    for col in df.select_dtypes(include=['object', 'category']):
        frequency_table = df[col].value_counts().reset_index()
        frequency_table.columns = ['Value', 'Frequency']
        
        frequency_table['Column'] = col
        frequency_table = frequency_table[['Column', 'Value', 'Frequency']]
        
        combined_results = pd.concat([combined_results, frequency_table], ignore_index=True)
    
    print(tabulate(combined_results, headers='keys', showindex=False))
    print()

def drop_missing_rows(df, threshold):
    rcount = df.shape[0]    
    df.dropna(thresh=threshold, inplace=True)
    print(f"Deleted rows with More than 50% Nulls :{rcount - df.shape[0]} rows")
    print()
    
def drop_features(df, features_list):
    for col in features_list:
        print(f"Dropping column :{col}")
        
        try:
            df.drop(columns=[col], inplace=True)
        except KeyError as err:
            print(f"No Column with name :{col}, error :{err}")
            exit(1)

    print(f"Deleted features :{len(features_list)}")
    print()

def impute_mean_at_missing(df, impute_features_list):
    for col in impute_features_list:
        df[col].fillna(df[col].mean(), inplace=True)

def impute_mode_at_missing(df, impute_features_list):
    for col in impute_features_list:
        df[col] = df[col].fillna(df[col].mode()[0])

def impute_missing_by_value(df, impute_features_list, value):
    for col in impute_features_list:
        df[col].fillna(value, inplace=True)

def handle_missing_data(df):
    threshold = df.shape[1] * 0.5  # delete if 50% of the values are missing
    drop_missing_rows(df, threshold)
    
    features_list = []
    drop_features(df, features_list)
    
    impute_features_list = []
    impute_mean_at_missing(df, impute_features_list)

    impute_features_list = []
    impute_mode_at_missing(df, impute_features_list)
    
    impute_features_list = []
    value = 0
    impute_missing_by_value(df, impute_features_list, value)
    
    print()

def visualize_numerical_features(df, features_list):
    num_features = len(features_list)
    if not num_features:
        return 
    
    fig, axes = plt.subplots(num_features, 2, figsize=(12, 5 * num_features))
    
    for i, col in enumerate(features_list):
        sns.histplot(df[col], bins=30, kde=True, ax=axes[i, 0])
        axes[i, 0].set_title(f'Histogram of {col}')
        axes[i, 0].set_xlabel(col)
        axes[i, 0].set_ylabel('Frequency')
        
        sns.boxplot(x=df[col], ax=axes[i, 1])
        axes[i, 1].set_title(f'Box Plot of {col}')
        axes[i, 1].set_xlabel(col)
        
    plt.tight_layout()
    plt.show()

def visualize_pairplot(df, features_list):
    if not len(features_list):
        return 
    
    sns.pairplot(df[features_list])
    plt.show()

def visualize_correlation_matrix(df, features_list):
    if not len(features_list):
        return 

    correlation_matrix = df.corr(features_list)
    fig, ax = plt.subplots(figsize=(8, 6))

    sns.heatmap(correlation_matrix, annot=True, cmap='YlOrRd', ax=ax)

    ax.set_title('Correlation Matrix')
    ax.set_xlabel('Numerical Features')
    ax.set_ylabel('Numerical Features')

    plt.tight_layout()
    plt.show()

def visualization_box_plot(df, pair):
    # plt.figure(figsize=(5, 5))
    plt.figure()
    # plt.subplot(2,3,1)
    sns.boxplot(x = pair[0], y = pair[1], data = df)
    plt.show()

def data_visualization(df):
    features_list = ["price", "area", "bedrooms", "bathrooms", "stories", "parking"]
    features_list = []
    visualize_numerical_features(df, features_list)
    
    features_list = ["area", "bedrooms", "price"]
    features_list = []
    visualize_pairplot(df, features_list)

    features_list = ["area", "bedrooms", "price"]
    features_list = []
    visualize_correlation_matrix(df, features_list)
    
    features_pairs = [
        ['mainroad', 'price'],
        ['guestroom', 'price'],
        ['basement', 'price'],
        ['hotwaterheating', 'price'],
        ['airconditioning', 'price'],
        ['furnishingstatus','price'],
    ]
    features_pairs = []
    for pair in features_pairs:
        visualization_box_plot(df, pair)

def binary_map(x):
    return x.map({'Legit': 1, "Fraud": 0})

def encode_Legit_Fraud(df, features_list):
    df[features_list] = df[features_list].apply(binary_map)

def categorical_to_indicator(df, feature):
    status = pd.get_dummies(df[feature], drop_first = True)
    df = pd.concat([df, status], axis = 1)
    
    df.drop([feature], axis = 1, inplace = True)    
    
    return df

def True_False_map(x):
    return x.map({True: 1, False: 0})

def encode_true_false(df, features_list):
    df[features_list] = df[features_list].apply(True_False_map)
    
def feature_engineering(df):
    features_list =  ['quality']
    encode_Legit_Fraud(df, features_list)
    
    indicator_features = []
    for feature in indicator_features:    
        df = categorical_to_indicator(df, feature)
    
    features_list = []
    # for feature in features_list:    
    #     encode_true_false(df, feature)

    # df['semi-furnished'] = df['semi-furnished'].astype(int)
    # df['unfurnished'] = df['unfurnished'].astype(int)
    
    return df

def eliminiate_duplicates(df):
    df.drop_duplicates(inplace = True)

def split_data(df):
    return train_test_split(df, test_size=0.2, random_state = 100)
    
def rescaling_features(df_train, df_test):
    scaler = MinMaxScaler()
    num_vars = ['area', 'bedrooms', 'bathrooms', 'stories', 'parking', 'price']
    df_train[num_vars] = scaler.fit_transform(df_train[num_vars])
    
    X_train = df_train.drop('price', axis = 1)
    y_train = df_train['price']
    
    # Add a constant, otherwise it will pass the line through origin and will not give us intercept
    X_train_lm = sm.add_constant(X_train)

    # Create a first fitted model
    lr = sm.OLS(y_train, X_train_lm).fit()
    print(round(lr.params,3))
    print(lr.summary())
    
    return X_train, y_train

def get_VIF(X_train):
    # Create a dataframe that will contain the names of all the feature variables and their respective VIFs
    vif = pd.DataFrame()
    vif['Features'] = X_train.columns
    vif['VIF'] = [variance_inflation_factor(X_train.values, i) for i in range(X_train.shape[1])]
    vif['VIF'] = round(vif['VIF'], 2)
    vif = vif.sort_values(by = "VIF", ascending = False)
    print(vif)

def eda(df):
    is_data_loaded(df)
    data_undertand_structure(df)
    check_missing_values(df)
    get_numerical_stats(df)
    data_quality(df)
    get_categorical_frequencies(df)
    handle_missing_data(df)
    data_visualization(df)

    df = feature_engineering(df)
    is_data_loaded(df)

    ind_features = df.drop(columns=["quality", "type"])
    is_data_loaded(ind_features)

    dep_features = df.drop(columns=["quality"])
    is_data_loaded(dep_features)

    is_data_loaded(df)
    eliminiate_duplicates(df)
    print(df.info())
    
    X_train, x_test, y_train, y_test = train_test_split(ind_features, dep_features, train_size=0.8)
    
    print("X_train ============:")
    print(X_train.info())
    print()
    print("y_train ============:")
    print(y_train.info())
    print()

    lin_reg = LinearRegression()
    lin_reg.fit(X_train, y_train)
    return
    print(lin_reg.coef_)
    return

    y_pred = lin_reg.predict(x_test)
    r2score = r2_score(y_test, y_pred)
    print(f"r2score :{r2score}")

    return

    df_train, df_test = split_data(df)
    X_train, y_train = rescaling_features(df_train, df_test)
    return

    get_VIF(X_train)

    X_train.drop(['semi-furnished', 'bedrooms'], axis = 1, inplace = True)
    lin_reg = LinearRegression()
    lin_reg.fit(X_train, y_train)
    print(lin_reg.coef_)

    vif = pd.DataFrame()
    vif['Features'] = X_train.columns
    vif['VIF'] = [variance_inflation_factor(X_train.values, i) for i in range(X_train.shape[1])]
    vif['VIF'] = round(vif['VIF'], 2)
    vif = vif.sort_values(by = "VIF", ascending = False)
    print(vif)

    y_train_price = lin_reg.predict(X_train)

    num_vars = ['area', 'bedrooms', 'bathrooms', 'stories', 'parking', 'price']
    scaler = MinMaxScaler()
    # df_train[num_vars] = scaler.fit_transform(df_train[num_vars])
    df_test[num_vars] = scaler.fit_transform(df_test[num_vars])
    df_test.describe()

    X_test = df_test.drop('price', axis = 1)
    y_test = df_test['price']
    X_test = X_test.drop(["bedrooms", "semi-furnished"], axis = 1)
    y_pred = lin_reg.predict(X_test)
    r2score = r2_score(y_test, y_pred)
    print(f"r2score :{r2score}")

    return
    apply_multicollinearity(df, OUTPUT_COLUMN)
    print(df.info())
    return
    
def main():
    data_set = get_dataset()
    df = pd.read_csv(data_set)
    eda(df)

if (__name__ == '__main__'):
    main()
