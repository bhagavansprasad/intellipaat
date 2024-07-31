import matplotlib.pyplot as plt

def sample_01():
    x = [1,2,3,4,5]
    y = [1000,2000,500,8000,3000]
    y1 = [1050,3000,2000,4000,6000]

    fig, ax1 = plt.subplots()

    ax2 = ax1.twinx()
    ax1.bar(x, y)
    ax2.plot(x, y1, 'o-', color="red" )

    ax1.set_xlabel('X data')
    ax1.set_ylabel('Counts', color='g')
    ax2.set_ylabel('Detection Rates', color='b')

    plt.show()


def sample_02():
    # Sample data
    years = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
    production = [200000, 300000, 500000, 700000, 600000, 800000, 900000, 850000, 950000]
    price = [50, 45, 40, 35, 30, 25, 20, 15, 10]

    fig, ax1 = plt.subplots()

    color = 'tab:blue'
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Production', color=color)
    ax1.plot(years, production, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    color = 'tab:red'
    ax2.set_ylabel('Price', color=color)
    ax2.plot(years, price, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()  # to make sure the labels don't overlap
    plt.title('Production vs Price over Years')
    plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def sample_03():
    # Sample data in a dictionary
    data = {
        'Year': [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
        'Production': [200000, 300000, 500000, 700000, 600000, 800000, 900000, 850000, 950000],
        'Price': [50, 75, 60, 90, 50, 30, 20, 15, 10]
    }

    # Creating a DataFrame
    df = pd.DataFrame(data)

    # Plotting
    fig, ax1 = plt.subplots()

    # Plotting Production
    sns.lineplot(data=df, x='Year', y='Production', ax=ax1, color='blue')
    ax1.set_ylabel('Production', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')

    # Creating a twin Axes sharing the x-axis
    ax2 = ax1.twinx()

    # Plotting Price
    sns.lineplot(data=df, x='Year', y='Price', ax=ax2, color='red')
    ax2.set_ylabel('Price', color='red')
    ax2.tick_params(axis='y', labelcolor='red')

    # Final plot adjustments
    plt.title('Production vs Price over Years')
    fig.tight_layout()  # to make sure the labels don't overlap
    plt.show()


def main():
    # sample_01()
    # sample_02()
    sample_03()
    
if (__name__ == '__main__'):
    main()

