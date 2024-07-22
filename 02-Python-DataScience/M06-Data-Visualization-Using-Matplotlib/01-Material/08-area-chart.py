import numpy as np
import matplotlib.pyplot as plt

def area_plot_01(): # line plot line chart
    x = range(1, 15)
    y = [1,4,6,8,4,5,3,2,4,1,5,6,8,7]
    
    plt.stackplot(x, y)
    plt.plot(x, y)
    plt.show()


def main():
    area_plot_01()
    pass
    
if __name__ == "__main__":
    main()
