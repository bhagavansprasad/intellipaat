import pandas as pd
import numpy as np
import sys

def list_to_dataframes():
    a = [10, 20, 30, 40, 50]
    sa = pd.Series(a)
    df = pd.DataFrame(a)
    
    print(f"a  type {type(a)}")
    print(f"sa type {type(sa)}")
    print(f"df type {type(df)}")
    print(f"sa      \n{sa}")
    print(f"df      \n{df}")

    print(f"a  size {sys.getsizeof(a)}")
    print(f"sa size {sys.getsizeof(sa)}")
    print(f"df size {sys.getsizeof(df)}")

def dict_to_dataframes():
    d = {'books' : ['python', 'C', 'R'], 'count': [100, 200, 300]}
    df = pd.DataFrame(d)
    
    print(f"d  type {type(d)}")
    print(f"df type {type(df)}")
    print(f"df      \n{df}")

    print(f"d  size {sys.getsizeof(d)}")
    print(f"df size {sys.getsizeof(df)}")

def series_to_dataframes():
    a = [10, 20, 30, 40, 50]
    sa = pd.Series(a)
    df = pd.DataFrame(sa)
    
    print(f"a  type {type(a)}")
    print(f"sa type {type(sa)}")
    print(f"df type {type(df)}")
    print(f"sa      \n{sa}")
    print(f"df      \n{df}")

    print(f"a  size {sys.getsizeof(a)}")
    print(f"sa size {sys.getsizeof(sa)}")
    print(f"df size {sys.getsizeof(df)}")

def numpy_to_dataframes():
    nparray = np.array([['Python', 'C', 'R'],[100, 200, 300]])
    print(f'nparray :{nparray}')
    
    df = pd.DataFrame({'books':nparray[0], 'pages':nparray[1]})
    
    print(f"nparray  type {type(nparray)}")
    print(f"df type       {type(df)}")
    print(f"nparray       \n{nparray}")
    print(f"df            \n{df}")

def main():
    # list_to_dataframes()
    # dict_to_dataframes()
    # series_to_dataframes()
    # numpy_to_dataframes()    
    
    pass

if __name__ == "__main__":
    main()
