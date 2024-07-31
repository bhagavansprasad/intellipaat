import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def basics_01():
    a = pd.read_csv('tips.csv')
    print(f"tips :{a}")
    
    x = a['total_bill']
    y = a['tip']
    
    plt.scatter(x, y)
    
    plt.show()

def basics_02():
    a = pd.read_csv('tips.csv')
   
    x = a['total_bill']
    y = a['tip']
    
    plt.scatter(x, y, s = 100)
    plt.xlabel('Total Bill')
    plt.ylabel('Tip')
    plt.title('Total Bill Vs Tip')
    
    plt.show()

def basics_03():
    a = pd.read_csv('tips.csv')
   
    x = a['total_bill']
    y = a['tip']
    
    plt.scatter(x, y, s = 100, color = 'green', marker = '*')
    plt.xlabel('Total Bill')
    plt.ylabel('Tip')
    plt.title('Total Bill Vs Tip')
    
    plt.show()
    
def main():
    # basics_01()
    # basics_02()
    basics_03()

if __name__ == "__main__":
    main()
    
    