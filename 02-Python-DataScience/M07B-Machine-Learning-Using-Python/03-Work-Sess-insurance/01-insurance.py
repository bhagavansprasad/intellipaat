import pandas as pd

# average mean of object datatypes

def eda_object_dtypes(idata):
    columns = idata.columns.to_list()
    print(columns)
    print(idata.describe())
    
    # for col in columns:
    #     if(idata.)
    
    # mean of 
    
    
def eda(idata):
    print(idata.head())
    print(idata.info())
    print(idata.shape)

    print(idata.isnull())
    print(idata.isnull().sum())
    print(idata.isnull().sum().sum())

    eda_object_dtypes(idata)
    return
    

def main():
    # EDA - Exploratory Data Analysis
        # Finding null values
            # Remove null values column wise
                # if column is object
                    #   replace with average value of the column
            
    for r in dir(pd):
        print(r)
    return

    insu_data = pd.read_csv("insurance_data.csv")
    eda(insu_data)
    

if (__name__ == '__main__'):
    main()
