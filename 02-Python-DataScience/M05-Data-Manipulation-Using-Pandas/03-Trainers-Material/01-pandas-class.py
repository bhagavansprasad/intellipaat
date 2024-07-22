import pandas as pd

def sample_01():
    a = pd.read_csv("market_fact.csv")
    print(f"a :{a}")
    
    print(f"shape      :{a.shape}")
    print(f"isnull     :{a.isnull()}")
    print(f"isnull sum :{a.isnull().sum()}")
    

def main():
    sample_01()

if __name__ == "__main__":
    main()