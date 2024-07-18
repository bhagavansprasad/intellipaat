import pandas as pd

def question_01():
    count = 0
    a = pd.read_csv('customer_churn-1.csv')

    f = (a['TechSupport'] == 'Yes') & (a['gender'] == 'Male') & (a['SeniorCitizen'] == True)
    print(f"data :{a[f]}")

    for r, c in a.iterrows():
        if (c['TechSupport'] == 'Yes' and c['gender'] == 'Male' and c['SeniorCitizen'] == True):
            count += 1
    print(f"count :{count}")

def main():
    question_01()
    
if __name__ == "__main__":
    main()
