import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def sample_01():
    df = pd.read_csv("country_profile_variables.csv")
    print(f"shape    :{df.shape}")
    print(f"describe :{df.describe()}")
    print(f"info     :{df.info()}")
    print(f"head     :{df.head()}")
    

def random_state():
    df = pd.read_csv("country_profile_variables.csv")
    # print(df.sample(2, random_state = 10))
    print(df["Population density (per km2, 2017)"].sample(2, random_state = 10))
    pass

def random_state_seed():
    df = pd.read_csv("country_profile_variables.csv")
    np.random.seed(10)
    print(df["Population density (per km2, 2017)"].sample(2, random_state = 10))
    pass

def mean_median_mode():
    df = pd.read_csv("country_profile_variables.csv")
    print(f"pd mean   :{df['Population density (per km2, 2017)'].mean()}")
    print(f"pd median :{df['Population density (per km2, 2017)'].median()}")
    print(f"pd mode   :{df['Population density (per km2, 2017)'].mode()}")

    print()
    
    print(f"np mean   :{np.mean(df['Population density (per km2, 2017)'])}")
    print(f"np median :{np.median(df['Population density (per km2, 2017)'])}")
    print(f"np mode   :{np.mode(df['Population density (per km2, 2017)'])}")
    pass

def trasnpose():
    df = pd.read_csv("country_profile_variables.csv")
    print(f"Transpose :{df.describe().T}")
    print(f"Transpose :{df.describe(include='O').T}")  #include only 'O'bject datatype
    print(f"Transpose :{df.describe(include='all').T}")  #include only 'O'bject datatype
    pass

def visualizing():
    df = pd.read_csv("country_profile_variables.csv")
    plt.figure(figsize=(10, 8))
    plt.hist(df['Population density (per km2, 2017)'])
    plt.show()
    pass

def main():
    # sample_01()
    # random_state()
    # random_state_seed()
    mean_median_mode()
    # trasnpose()
    # visualizing()
    
    pass

if (__name__ == "__main__"):
    main()