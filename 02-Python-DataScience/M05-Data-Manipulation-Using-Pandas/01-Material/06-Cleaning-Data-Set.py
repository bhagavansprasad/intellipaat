import pandas as pd

def rename_column():
    cars = pd.read_csv('cars.csv')
    print(f"cars             :\n{cars}")
    
    cars = cars.rename(columns = {'Unnamed: 12': 'newcolumn'})
    print(f"cars             :\n{cars}")

def fill_null_with_median():
    cars = pd.read_csv('cars.csv')
    print(f"cars             :\n{cars}")
    
    cars.qsec = cars.qsec.fillna(cars.qsec.mean())
    print(f"cars             :\n{cars}")

    cars = cars.drop(columns=['S.No'])
    print(f"cars             :\n{cars}")

def columns_correlation():
    cars = pd.read_csv('cars.csv')
    print(f"cars             :\n{cars}")
    
    cars = cars[['model', 'mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'Unnamed: 12']].corr()
    print(f"cars             :\n{cars}")
    
    cars.mpg = cars.mpg.astype(float)
    print(f"cars             :\n{cars}")
    
    cars.info(null_counts=True)
    
def cleaning_data():
    # rename_column()
    # fill_null_with_median()
    columns_correlation()
    
def main():
    cleaning_data()
    pass

if __name__ == "__main__":
    main()
