import pandas as pd

def question_01(): #df: sort based on column in reverse order
    a = pd.read_csv('customer_churn-1.csv')
    a.sort_values(by='tenure', ascending=False)
    print(f"a :\n{a}")

def question_02(): # df: filerting data 
    a = pd.read_csv('customer_churn-1.csv')

    f = (a['tenure'] > 50) & (a['gender'] == 'Female')
    print(f"data :{a[f]}")

    f = (a['SeniorCitizen'] == False) & (a['gender'] == 'Male')
    print(f"data :{a[f]}")

    f = (a['TechSupport'] == 'Yes') & (a['Churn'] == 'No')
    print(f"data :{a[f]}")

    f = (a['Contract'] == 'Month-to-month') & (a['Churn'] == 'Yes')
    print(f"data :{a[f]}")

def main():
    question_01()
    question_02()
    
if __name__ == "__main__":
    main()
