import pandas as pd
import matplotlib.pyplot as plt 
# %matplotlib inline

def line_plot_01():
    cars = pd.read_csv('cars.csv')
    # print(f"cars             :\n{cars}")
    
    # line plot
    y1 = cars['hp']
    x = range(32)
    plt.plot(x, y1)
    plt.show()

    # line plot
    y2 = cars['disp']
    x = range(32)
    plt.plot(x, y2)
    plt.show()

def line_plot_02():
    cars = pd.read_csv('cars.csv')
    
    y1 = cars['hp']
    y2 = cars['disp']
    x = range(32)

    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.show()

def area_plot():
    cars = pd.read_csv('cars.csv')
    
    y1 = cars['hp']
    y2 = cars['disp']
    x = range(32)

    plt.stackplot(x, y1, alpha = 0.7)
    plt.stackplot(x, y2, alpha = 0.5)
    plt.show()

    plt.stackplot(x, y1)
    plt.stackplot(x, y2)
    plt.show()

    plt.plot(x, y1, linewidth = 2.0, color = 'c')
    plt.stackplot(x, y1, alpha = 0.7)

    plt.plot(x, y2, linewidth = 2.0, color = 'r')
    plt.stackplot(x, y2, alpha = 0.7)

    plt.show()

def bar_plot():
    cars = pd.read_csv('cars.csv')
    
    y = cars['hp']
    x = range(32)

    x1 = cars['model'].tolist()
    
    fig = plt.figure(figsize = (15, 10))
    plt.bar(x1, y, color='purple', alpha=0.9)
    plt.show()

    plt.barh(x1, y, color='purple', alpha=0.9)
    plt.show()
        
    
def main():
    line_plot_01()
    line_plot_02()
    area_plot()
    bar_plot()
    pass

if __name__ == "__main__":
    main()
