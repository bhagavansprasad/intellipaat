import pandas as pd
import numpy as np

def range_series(sp = 1, ep=10):
    return pd.Series(range(sp, ep+1))

def sum_arrays(*arrays): # np array adding adding arrays
    summed_array = np.sum(arrays, axis=0)
    return summed_array
    
def question_01():
    s1 = range_series()
    s2 = range_series(5)
    s3 = range_series(5, 10)
    
    print(f"s1 :\n{s1}")
    print(f"s2 :\n{s2}")
    print(f"s3 :\n{s3}")
    
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])
    c = np.array([[9, 10], [11, 12]])

    s = sum_arrays(a, b, c)
    print (f"s :\n{s}")

def create_dataframe(keys, values):

    # df = pd.DataFrame({keys[0]: values[0], keys[1]: values[1]}, index=[0, 1])
    d = {}
    idx = []
    for i, key in enumerate(keys):
        d[key] = values[i]
        idx.append(i)
 
    return pd.DataFrame(d, index=idx)

def question_02():
    df1 = create_dataframe(["One", "Two"], [["X", "Y"], ["A", "B"]])
    df2 = create_dataframe(["One", "Two", "Three"], [["X", "Y", "Z"], ["A", "B", "C"], ["m", "n", "o"]])

    print (f"df1 :\n{df1}")
    print (f"df2 :\n{df2}")
    
def question_03():
    df1 = create_dataframe(["One", "Two"], [["X", "Y"], ["A", "B"]])
    df2 = create_dataframe(["One", "Two", "Three"], [["X", "Y", "Z"], ["A", "B", "C"], ["m", "n", "o"]])

    print (f"df1 :\n{df1}")
    print (f"df2 :\n{df2}")
    
    df = pd.concat([df1, df2]).reset_index()
    print (f"df :\n{df}")

def question_04():
    cars = pd.read_csv('cars.csv')
    
    # print(f"cars count     :\n{cars.count()}")
    # print(f"cars mean      :\n{cars.mean()}")
    # print(f"cars median    :\n{cars.median()}")
    # print(f"cars std       :\n{cars.std()}")
    # print(f"cars min       :\n{cars.min()}")
    # print(f"cars max       :\n{cars.max()}")
    print(f"cars describe  :\n{cars.describe()}")

def question_05():
    cars = pd.read_csv('cars.csv')
    # print(f"cars           :\n{cars}")
    print(f"cars describe  :\n{cars.describe()}")
      
def main():
    # question_01()
    # question_02()
    # question_03()
    # question_04()
    question_05()
    
if __name__ == "__main__":
    main()
