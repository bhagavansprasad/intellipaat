import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

def vis_data_set_01():
    cusomer = pd.read_csv('customer_churn-1.csv')
    print(cusomer.head())  
    
    print(cusomer['InternetService'].value_counts())
    print(cusomer['InternetService'].value_counts().keys().tolist())
    
    plt.bar(cusomer['InternetService'].value_counts().keys().tolist(), 
                  cusomer['InternetService'].value_counts().tolist())

    plt.show()
    
def main():
    vis_data_set_01()
    pass
    
if __name__ == "__main__":
    main()
