import pandas as pd

def question_01():
    a = pd.read_csv('customer_churn-1.csv')
    print(f"a df :\n{a}")

def question_02(): # df: read selected columns by index
    a = pd.read_csv('customer_churn-1.csv')
    print(f"a df :\n{a}")
    
    # print(f"3: {a.columns[3]}, 7: {a.columns[7]}, 9: {a.columns[9]}, 20: {a.columns[20]}")
    # print(f"df :{a[[a.columns[3], a.columns[7], a.columns[9], a.columns[20]]]}")
    newCols = pd.DataFrame(a[[a.columns[3], a.columns[7], a.columns[9], a.columns[20]]])
    print(f"newCols df :\n{newCols}")

def question_03(): # df: read rows by index range
    a = pd.read_csv('customer_churn-1.csv')
    print(f"a df   :\n{a}")
    print(f"a type :\n{type(a)}")
    
    newCols = a.iloc[200:1001]
    print(f"newCols df :\n{newCols}")

# row 20:200, col 2:15th
def question_04(): # df: row index range and column index range
    a = pd.read_csv('customer_churn-1.csv')
    print(f"a df   :\n{a}")
    print(f"a type :\n{type(a)}")
    
    na = a.iloc[200:1001]
    newCols = pd.DataFrame(na[na.columns[3:16]])
    print(f"newCols df :\n{newCols}")
    
def question_05(): # df: top 10 records
    a = pd.read_csv('customer_churn-1.csv')
    print(f"a head 100 :\n{a.head(100)}")

def question_06(): # df: tail last 10 records
    a = pd.read_csv('customer_churn-1.csv')
    print(f"a tail 10 :\n{a.tail(10)}")

def question_07(): # df: last record
    a = pd.read_csv('customer_churn-1.csv')
    
    print(f"Last record {a.iloc[-1]}")

def question_08(): #df: sort based on column in reverse order
    a = pd.read_csv('customer_churn-1.csv')
    a.sort_values(by='tenure', ascending=False)
    print(f"a :\n{a}")

def question_09(): # df: filerting data 
    a = pd.read_csv('customer_churn-1.csv')

    f = (a['tenure'] > 50) & (a['gender'] == 'Female')
    print(f"data :{a[f]}")

    f = (a['SeniorCitizen'] == False) & (a['gender'] == 'Male')
    print(f"data :{a[f]}")

    f = (a['TechSupport'] == 'Yes') & (a['Churn'] == 'No')
    print(f"data :{a[f]}")

    f = (a['Contract'] == 'Month-to-month') & (a['Churn'] == 'Yes')
    print(f"data :{a[f]}")

def question_10():
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
    question_02()
    question_03()
    question_04()
    question_05()
    question_06()
    question_07()
    question_08()
    question_09()
    question_10()
    
if __name__ == "__main__":
    main()
