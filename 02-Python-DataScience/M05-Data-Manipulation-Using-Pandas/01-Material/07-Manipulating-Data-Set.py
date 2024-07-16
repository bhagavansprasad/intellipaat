import pandas as pd

def manipulating_data():
    cars = pd.read_csv('cars.csv')
    print(f"cars             :\n{cars}")
    
    print(cars.iloc[:,4])
    print(cars.iloc[0:4,4])
    print(cars.iloc[:,:])
    print(cars.iloc[6:,4:])
    print(cars.iloc[:,:1])
    print(cars.loc[:,"mpg"])
    print(cars.loc[:,"mpg":"qsec"])
    
    cars['am'] = 1
    print(cars)
    
    f = lambda x: x * 2
    cars['am'] = cars["am"].apply(f)
    print(cars)

    cars = cars.sort_values(by='cyl')
    print(cars)

    cars = cars.sort_values(by='cyl', ascending=False)
    print(cars)
    
    print(cars['cyl'] > 6)
    filter = cars['cyl'] > 6
    filtered_new = cars[filter]
    print(filtered_new)
    print()
    
    filter = (cars['cyl'] > 6) & (cars['hp'] > 300) 
    filtered_new = cars[filter]
    print(filtered_new)
    print()

def main():
    manipulating_data()
    pass

if __name__ == "__main__":
    main()
