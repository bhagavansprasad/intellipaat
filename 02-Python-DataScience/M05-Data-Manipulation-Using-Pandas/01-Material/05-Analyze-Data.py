import pandas as pd

def analyze_dataset():
    cars = pd.read_csv('cars.csv')
    
    print(f"cars             :\n{cars}")
    print(f"cars type        :{type(cars)}")
    print(f"cars head        :\n{cars.head()}")
    print(f"cars head(10)    :\n{cars.head(10)}")
    
    print(f"cars tail        :\n{cars.tail()}")
    print(f"cars tail(10)    :\n{cars.tail(10)}")
    
    print(f"cars shape       :\n{cars.shape}")
    print(f"cars info nulls  :\n{cars.info(null_counts=True)}")

    print(f"cars mean      :\n{cars.mean()}")
    print(f"cars median    :\n{cars.median()}")
    print(f"cars std       :\n{cars.std()}")
    print(f"cars max       :\n{cars.max()}")
    print(f"cars min       :\n{cars.min()}")
    print(f"cars count     :\n{cars.count()}")
    print(f"cars describe  :\n{cars.describe()}")
    


def main():
    analyze_dataset()
    pass

if __name__ == "__main__":
    main()
