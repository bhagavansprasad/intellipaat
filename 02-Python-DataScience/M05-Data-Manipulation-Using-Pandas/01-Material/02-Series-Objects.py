import pandas as pd 

def different_data_types():
    a = [1, 2, 3, 4, 5]
    sa = pd.Series(a)
    
    print(f"a  type {type(a)}")
    print(f"sa type {type(sa)}")
    print(f"sa      \n{sa}")

    sa = pd.Series(a, index=list(range(1, len(a)+1)))
    print(f"sa      \n{sa}")

    sa = pd.Series(a, index=['a', 'b', 'c', 'd', 'e'])
    print(f"sa      \n{sa}")

def main():
    different_data_types()
    
    pass

if __name__ == "__main__":
    main()
