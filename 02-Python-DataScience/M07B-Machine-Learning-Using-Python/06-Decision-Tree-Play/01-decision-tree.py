import pandas as pd
import math

DATA_SET =  "PlayTennis.csv"
OUTPUT_COLUMN = "play"
OUTPUT_VALUES = ["yes", "no"]

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

def eda(df):
    is_data_loaded(df)
    data_undertand_structure(df)

def get_entropy(values, values_count):
    S = 0.0
    
    for key in values:
        fvalue = values[key]/values_count
        # print(f"key :{key}, count :{values[key]}, tot :{values_count}, fvalue :{fvalue}")
        S = S - (fvalue * math.log(fvalue, 2))

    return S.round(4)

def get_gain(df, attribute, output_feature, S):
    print()
    unique_values = df[attribute].unique()
    row_count = df.shape[0]
    t = 0

    print(f"Attribute :{attribute}, Values({attribute}) :{unique_values}")
    
    for v in unique_values:
        print(f"\tS({v})", end=": ")
        filter = df[attribute] == v
        filtered_df = df[filter]

        values_count = filtered_df[output_feature].count()
        values = dict(filtered_df.groupby(output_feature)[output_feature].count())

        S1 = get_entropy(values, values_count)
        print(f"values_count :{values_count}, row_count :{row_count}, Values :{values}, E({v}) :{S1}")
        t = t + (values_count/row_count) * S1

    Gain = S - t
    Gain = Gain.round(4)
    print(f"\tGain({attribute}) :{Gain}")
    
    return Gain

def maxvalue(r):
    # print(list(r.items())[0][1])
    return list(r.items())[0][1]

def get_entropy_by_frame(df, output_feature, col_values):
    # print(df[output_feature])
    values_count = df[output_feature].count()
    values = dict(df.groupby(output_feature)[output_feature].count())
    Gains = []
    
    print(f"S('{OUTPUT_COLUMN}') :values_count :{values_count}, Values :{values}")
    
    S = get_entropy(values, values_count)
    print(f"E('{OUTPUT_COLUMN}') :{S}")

    columns = list(df.columns)
    columns.remove(OUTPUT_COLUMN)
    
    for col in columns:
        t = get_gain(df[[col, OUTPUT_COLUMN]], col, OUTPUT_COLUMN, S)
        Gains.append({col:t})
    
    sorted(Gains, key=maxvalue)
    max_gain_col = list(Gains[0].keys())[0]

    print(f"Gains :{Gains}")    
    print(f"Max Gain :{Gains[0]}, feature :{max_gain_col}")
    print("-" * 100)
   
    print()
    return max_gain_col
    
def main():
    data_set = get_dataset()
    df = pd.read_csv(data_set)
    # eda(df)
    
    while(True):
        feture_column = get_entropy_by_frame(df, OUTPUT_COLUMN, OUTPUT_VALUES)
        unique_values = df[feture_column].unique()
        
        for uv in unique_values:
            filter = df[feture_column] == uv
            filter_df = df[filter]
            filter_df.drop(columns=[feture_column], inplace=True)
            print(filter_df)
            
        
        break

if (__name__ == '__main__'):
    main()
