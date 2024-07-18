import pandas as pd

def question_01(): # df: top 10 records
    a = pd.read_csv('customer_churn-1.csv')
    print(f"a head 100 :\n{a.head(100)}")

def question_02(): # df: tail last 10 records
    a = pd.read_csv('customer_churn-1.csv')
    print(f"a tail 10 :\n{a.tail(10)}")

def question_03(): # df: last record
    a = pd.read_csv('customer_churn-1.csv')
    
    print(f"Last record {a.iloc[-1]}")

def main():
    question_01()
    question_02()
    question_03()
    
if __name__ == "__main__":
    main()
