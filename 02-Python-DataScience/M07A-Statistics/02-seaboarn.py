import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def seaborn_basic_graph_01():
    tips = pd.read_csv("tips.csv")
    
    print(tips.head())
    
    sns.relplot(x = 'total_bill', y = 'tip', data = tips, kind = 'scatter')
    plt.show()

def seaborn_data_segregation_hue():
    tips = pd.read_csv("tips.csv")
    
    print(tips.head())
    
    sns.relplot(x = 'total_bill', y = 'tip', data = tips, kind = 'scatter', hue = 'sex')
    plt.show()

def seaborn_sns_style_hue_02():
    tips = pd.read_csv("tips.csv")
    
    print(tips.head())
    sns.set()
    
    sns.relplot(x = 'total_bill', y = 'tip', data = tips, kind = 'scatter', hue = 'day')
    plt.show()

def seaborn_sns_style_hue_03():
    tips = pd.read_csv("tips.csv")
    
    print(tips.head())
    sns.set()
    
    sns.relplot(x = 'total_bill', y = 'tip', data = tips, kind = 'scatter', hue = 'smoker', col = 'sex')
    plt.show()

def seaborn_sns_style_hue_04():
    tips = pd.read_csv("tips.csv")
    
    print(tips.head())
    sns.set()
    
    sns.relplot(x = 'total_bill', y = 'tip', data = tips, kind = 'scatter', hue = 'day', col = 'sex')
    plt.show()

def seaborn_line_plot_01():
    flights = pd.read_csv("flights.csv")
    
    print(flights.head())
    sns.set()
    
    sns.relplot(x = 'year', y = 'passengers', data = flights, kind = 'line')
    plt.show()

def seaborn_line_n_scatter_plot_02():
    flights = pd.read_csv("flights.csv")
    
    print(flights.head())
    sns.set()
    
    sns.relplot(x = 'year', y = 'passengers', data = flights, kind = 'line', hue='passengers')
    sns.relplot(x = 'year', y = 'passengers', data = flights, kind = 'scatter', hue='passengers')
    plt.show()

def seaborn_line_plot_03():
    flights = pd.read_csv("flights.csv")
    
    print(flights.head())
    sns.set()
    
    sns.relplot(x = 'year', y = 'passengers', data = flights, kind = 'line', hue='month')
    plt.show()

def seaborn_line_plot_04():
    flights = pd.read_csv("flights.csv")
    
    print(flights.head())
    sns.set()
    
    sns.relplot(x = 'year', y = 'passengers', data = flights, kind = 'line', hue='month', col = 'month')
    plt.show()

def seaborn_line_plot_05():
    flights = pd.read_csv("flights.csv")
    
    print(flights.head())
    sns.set()
    
    sns.relplot(x = 'year', y = 'passengers', data = flights, kind = 'line', hue='month', col = 'month')
    plt.show()

def seaborn_box_plot_01():
    tips = pd.read_csv("tips.csv")
    
    print(tips.head())
    
    # sns.catplot(x = 'total_bill', y = 'sex', data = tips, kind = 'box')
    sns.catplot(x = 'sex', y = 'total_bill', data = tips, kind = 'box')
    plt.show()
    
    # sns.relplot(x = 'year', y = 'passengers', data = flights, kind = 'box')
    # sns.relplot(x = 'year', y = 'passengers', data = flights, kind = 'box', hue='month', col = 'month')
    # sns.relplot(x = 'year', y = 'passengers', data = flights, kind = 'box', hue='month', col = 'month')
    plt.show()

def seaborn_count_plot_01():
    tips = pd.read_csv("tips.csv")
    
    print(tips.head())
    
    sns.countplot(x = 'sex', data = tips)
    plt.show()

def seaborn_count_plot_02():
    tips = pd.read_csv("tips.csv")
    
    print(tips.head())
    
    sns.countplot(x = 'smoker', data = tips)
    plt.show()

def seaborn_count_plot_03():
    tips = pd.read_csv("tips.csv")
    
    print(tips.head())
    
    sns.countplot(x = 'smoker', data = tips, hue = 'sex')
    plt.show()

def seaborn_count_plot_04():
    tips = pd.read_csv("tips.csv")
    
    print(tips.head())
    
    sns.countplot(x = 'sex', data = tips, hue = 'smoker')
    plt.show()

def seaborn_regression_plot_01():
    tips = pd.read_csv("tips.csv")
    
    print(tips.head())
    
    sns.regplot(x = 'total_bill', y= 'tip', data = tips)
    plt.show()

def seaborn_distribution_plot_01():
    tips = pd.read_csv("tips.csv")
    
    print(tips.head())
    
    sns.displot(x = 'total_bill', data = tips)
    plt.show()

def seaborn_kde_plot_01():
    tips = pd.read_csv("tips.csv")
    
    print(tips.head())
    
    sns.kdeplot(x = 'total_bill', data = tips)
    plt.show()
    
def seaborn_pair_plot_01():
    iris = pd.read_csv("iris.csv")
    
    print(iris.head())
    
    sns.pairplot(iris)
    plt.show()

def seaborn_pair_plot_02():
    iris = pd.read_csv("iris.csv")
    
    print(iris.head())
    
    sns.pairplot(iris, hue='species')
    plt.show()

def main():
    # seaborn_basic_graph_01()
    # seaborn_data_segregation_hue()
    # seaborn_sns_style_hue_03()
    # seaborn_sns_style_hue_04()
    # seaborn_line_plot_01()
    # seaborn_line_n_scatter_plot_02()
    # seaborn_line_plot_03()
    # seaborn_line_plot_04()
    # seaborn_line_plot_05()
    # seaborn_box_plot_01()
    # seaborn_count_plot_01()
    # seaborn_count_plot_02()
    # seaborn_count_plot_03()
    # seaborn_count_plot_04()
    # seaborn_regression_plot_01()
    # seaborn_distribution_plot_01()
    # seaborn_kde_plot_01()
    # seaborn_pair_plot_01()
    seaborn_pair_plot_02()
    
if (__name__ == '__main__'):
    main()

