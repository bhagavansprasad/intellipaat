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

def production_vs_stocks():
    hf = pd.read_csv("us_honey_dataset.csv")
    hf = hf.drop(columns=["Unnamed: 0"])
    hf.duplicated()

    print(hf.head())

    sns.lineplot(x = 'year', y = 'production', data = hf, label='production', errorbar=None, marker='o')
    sns.lineplot(x = 'year', y = 'stocks', data = hf, label='stocks', errorbar=None, marker='*')
    sns.despine()
    plt.title('Production vs Stocks')
    plt.grid(True)
    plt.show()


def production_vs_price():
    hf = pd.read_csv("us_honey_dataset.csv")
    hf = hf.drop(columns=["Unnamed: 0"])
    hf.duplicated()

    print(hf.head())
    
    fig, ax1 = plt.subplots()
    palette = sns.color_palette()

    sns.lineplot(x='year', y='production', data=hf, ax=ax1, label='Production', errorbar=None, marker='o', color='blue')

    ax2 = ax1.twinx()

    sns.lineplot(x='year', y='average_price', data=hf, ax=ax2, label='Price', errorbar=None, marker='*', color='red')

    sns.despine()
    plt.title('Production vs Price')
    plt.grid(True)
    fig.tight_layout()  # to make sure the labels don't overlap
    plt.show()

def colonies_and_yields():
    hf = pd.read_csv("us_honey_dataset.csv")
    hf = hf.drop(columns=["Unnamed: 0"])
    hf.duplicated()

    print(hf.head())
    
    fig, ax1 = plt.subplots()
    palette = sns.color_palette()

    sns.lineplot(x='year', y='colonies_number', data=hf, ax=ax1, label='colonies_number', errorbar=None, marker='o', color='blue')

    ax2 = ax1.twinx()

    sns.lineplot(x='year', y='yield_per_colony', data=hf, ax=ax2, label='yield_per_colony', errorbar=None, marker='*', color='red')

    sns.despine()
    plt.title('Colony count Vs Yield per Colony')
    plt.grid(True)
    fig.tight_layout()  # to make sure the labels don't overlap
    plt.show()

def colonies_vs_production():
    hf = pd.read_csv("us_honey_dataset.csv")
    hf = hf.drop(columns=["Unnamed: 0"])
    hf.duplicated()

    print(hf.head())
    
    fig, ax1 = plt.subplots()
    palette = sns.color_palette()

    sns.lineplot(x='year', y='colonies_number', data=hf, ax=ax1, label='colonies_number', errorbar=None, marker='o', color='blue')

    ax2 = ax1.twinx()

    sns.lineplot(x='year', y='production', data=hf, ax=ax2, label='production', errorbar=None, marker='*', color='red')

    sns.despine()
    plt.title('Colony count Vs Production')
    plt.grid(True)
    fig.tight_layout()  # to make sure the labels don't overlap
    plt.show()

def Multiple_graphs():
    hf = pd.read_csv("us_honey_dataset.csv")
    hf = hf.drop(columns=["Unnamed: 0"])
    hf.duplicated()

    print(hf.head())
    
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    fig.suptitle('US Honey Production Trend Over the years')

    sns.lineplot(ax = axes[0],         x='year', y='production', data=hf, label='Production', errorbar=None, marker='o', color='blue')
    sns.lineplot(ax = axes[0].twinx(), x='year', y='average_price', data=hf, label='Price', errorbar=None, marker='*', color='red')

    sns.lineplot(ax = axes[1],         x='year', y='colonies_number', data=hf, label='colonies_number', errorbar=None, marker='o', color='blue')
    sns.lineplot(ax = axes[1].twinx(), x='year', y='yield_per_colony', data=hf, label='yield_per_colony', errorbar=None, marker='*', color='red')

    sns.lineplot(ax = axes[2],         x='year', y='production', data=hf, label='production', errorbar=None, marker='*', color='red')
    sns.lineplot(ax = axes[2].twinx(), x='year', y='colonies_number', data=hf, label='colonies_number', errorbar=None, marker='o', color='blue')
    

    sns.despine()
    plt.title('Colony count Vs Production')
    plt.grid(True)
    fig.tight_layout()  # to make sure the labels don't overlap
    plt.show()

def point_plot():
    hf = pd.read_csv("us_honey_dataset.csv")
    hf = hf.drop(columns=["Unnamed: 0"])
    hf.duplicated()

    print(hf.head())
    
    sns.pointplot(data=hf, x="year", y="colonies_number")
    plt.show()

def main():
    # us_honey_scatter_graph_01()
    # us_honey_line_graph_01()
    # us_honey_pair_plot()
    # production_vs_stocks()
    # production_vs_price()
    # colonies_and_yields()
    # colonies_vs_production()
    # Multiple_graphs()
    point_plot()
    
if (__name__ == '__main__'):
    main()

