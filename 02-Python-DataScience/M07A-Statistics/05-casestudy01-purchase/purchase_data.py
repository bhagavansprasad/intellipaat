import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def data_info():
    df = pd.read_csv("purchase_data.csv")
    print(df.head())
    print(df.describe())
    print(df.info())
    print(df.shape)
    
    # Print Unique values in a column
    print(df['Stay_In_Current_City_Years'].unique())
    df['Stay_In_Current_City_Years'] = df['Stay_In_Current_City_Years'].replace("4+", "4")
    print(df['Stay_In_Current_City_Years'].unique())

    # Change column datatype
    # df['Stay_In_Current_City_Years'] = pd.to_numeric(df['Stay_In_Current_City_Years'])
    df['Stay_In_Current_City_Years'] = pd.to_numeric(df['Stay_In_Current_City_Years'], downcast='integer')
    df['Stay_In_Current_City_Years'] = pd.to_numeric(df['Stay_In_Current_City_Years'], downcast='float')
    print(df.info())
    
    # Replace NaN with 0
    df['Product_Category_1'].fillna(0, inplace=True)
    df['Product_Category_2'].fillna(0, inplace=True)
    df['Product_Category_3'].fillna(0, inplace=True)

    print(df.head())
    
    # Count of Null based on columns
    print(df.isnull().sum())
    
    # Total Count of Null in rows and columns
    print(df.isnull().sum().sum())
    
    # Duplicate rows count
    print(df.duplicated().sum())
    
    for col in df.columns:
        print(col, type(col))
    
    print(df.info())
    print(df.isnull().sum())
    print()
    for col in df.columns:
        if (df[col].dtype != "object"):
            df[col] = df[col].astype(int)
    print(df.info())
    

# Gender Vs Purchase
def Gender_Vs_Purchase():
    pass 
# 1. It was observed that the average purchase made by the Men of the age 18-25 was 10000. Is it still the same?
# ['P00000142' 'P00000242' 'P00000342' ... 'P0099742' 'P0099842' 'P0099942']
# ['F' 'M']
# ['0-17' '18-25' '26-35' '36-45' '46-50' '51-55' '55+']
# ['A' 'B' 'C']
# filter = ((df['Gender'] == 1) & df['Purchase'] > 10000)

# 2. It was observed that the percentage of women of that spend more than 10000 was 35%. Is it still the same?
# 3. Is the average purchase made by men and women of the age 18-25 same?
# 4. Is the percentage of men who have spent more than 10000 the same for the ages 18-25 and 26-35?

# Gender vs P1
# Age Vs P1
# Occupation Vs P1
# City Vs P1
    
# #   Column                      Dtype
# ---  ------                      -----
#  0   User_ID                     int64
#  1   Product_ID                  object
#  2   Gender                      object
#  3   Age                         object
#  4   Occupation                  float64
#  5   City_Category               object
#  6   Stay_In_Current_City_Years  object
#  7   Marital_Status              float64
#  8   Product_Category_1          float64
#  9   Product_Category_2          float64
#  10  Product_Category_3          float64
#  11  Purchase                    float64    

def main():
    data_info()
    
if (__name__ == '__main__'):
    main()

