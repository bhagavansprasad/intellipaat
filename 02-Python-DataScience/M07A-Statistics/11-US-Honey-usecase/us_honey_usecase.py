import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def us_honey_scatter_graph_01():
    hf = pd.read_csv("us_honey_dataset.csv")
    
    print(hf.head())
    
    sns.relplot(x = 'year', y = 'production', data = hf, kind = 'scatter')
    plt.show()

    sns.relplot(x = 'year', y = 'production', data = hf, kind = 'scatter', hue='average_price')
    plt.show()

def us_honey_line_graph_01():
    hf = pd.read_csv("us_honey_dataset.csv")
    hf = hf.drop(columns=["Unnamed: 0"])
        
    shape = hf.shape
    print(f"shape :{shape}")
    
    hf.duplicated()
    shape = hf.shape
    print(f"shape after removing duplicates :{shape}")

def us_honey_pair_plot():
    hf = pd.read_csv("us_honey_dataset.csv")
    hf = hf.drop(columns=["Unnamed: 0"])
    hf.duplicated()

    print(hf.head())

    sns.pairplot(hf)
    plt.show()

def multi_line_graph_01():
    hf = pd.read_csv("us_honey_dataset.csv")
    hf = hf.drop(columns=["Unnamed: 0"])
    hf.duplicated()
    
    print(hf.head())

    sns.lineplot(x = 'year', y = 'production', data = hf, label='production', errorbar=None, marker='o')
    sns.lineplot(x = 'year', y = 'stocks', data = hf, label='stocks', errorbar=None, marker='*')
    sns.despine()
    plt.grid(True)
    plt.show()


def multi_line_graph_02():
    hf = pd.read_csv("us_honey_dataset.csv")
    hf = hf.drop(columns=["Unnamed: 0"])
    hf.duplicated()
    
    hf = hf.drop("state", axis = 1).groupby("year").mean()
    sns.lineplot(x = 'year', y = 'production', data = hf, label='production', errorbar=None, marker='o')
    sns.lineplot(x = 'year', y = 'average_price', data = hf, label='average_price', errorbar=None, marker='*')
    sns.despine()
    plt.grid(True)
    plt.show()

def main():
    # us_honey_scatter_graph_01()
    # us_honey_line_graph_01()
    # us_honey_pair_plot()
    # multi_line_graph_01()
    multi_line_graph_02()

if (__name__ == '__main__'):
    main()

