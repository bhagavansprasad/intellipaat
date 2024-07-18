import pandas as pd

# row 20:200, col 2:15th
def question_01(): # df: row index range and column index range
    a = pd.read_csv('customer_churn-1.csv')
    
    na = a.iloc[20:201]
    newCols = pd.DataFrame(na[na.columns[2:16]])
    print(f"newCols df :\n{newCols}")

def main():
    question_01()
    
if __name__ == "__main__":
    main()
