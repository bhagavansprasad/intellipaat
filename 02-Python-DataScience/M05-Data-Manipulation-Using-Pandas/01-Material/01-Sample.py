import pandas as pd

def sample_01(): #loc vs iloc
    a = pd.read_csv('customer_churn-1.csv')
    print(a)
    # print(a[3])
    print(a.loc[3])
    print(a.iloc[3])
    print(a.iloc[3,5])
    # print(a.iloc[3, "customerID"])
    print(a.loc[3, ["customerID", "Contract"]])
    print(a.tenure < 40) 
    print((a.tenure > 20) & (a.tenure < 40)) 
    print()
    print(a[(a.tenure > 20) & (a.tenure < 40)])
    
def main():
    sample_01()
    
    pass

if __name__ == "__main__":
    main()
