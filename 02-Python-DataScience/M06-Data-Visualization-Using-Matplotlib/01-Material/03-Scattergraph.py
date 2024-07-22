import numpy as np
import matplotlib.pyplot as plt

def scatter_plot_01(): # scatter plot
    # a = list(np.arange(10, 90, 10))
    # b = list(np.random.randint(1, 10, 8))
    # x = list(np.random.randint(1, 4, 8))
    a = [10, 20, 30, 40, 50, 60, 70, 80]
    b = [3, 1, 8, 9, 3, 7, 3, 8]
    x = [2, 3, 2, 2, 1, 2, 3, 2]
    
    plt.scatter(a, b)
    plt.scatter(a, x)
    plt.show()

def scatter_plot_02(): 
    a = [10, 20, 30, 40, 50, 60, 70, 80]
    b = [3, 1, 8, 9, 3, 7, 3, 8]
    x = [2, 3, 2, 2, 1, 2, 3, 2]
    
    plt.scatter(a, b)
    plt.scatter(a, x)
    plt.legend(['b', 'x'], loc='best')
    plt.title('Scatter Plot Demo')
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    plt.show()

def scatter_plot_03(): 
    a = [10, 20, 30, 40, 50, 60, 70, 80]
    b = [3, 1, 8, 9, 3, 7, 3, 8]
    x = [2, 3, 2, 2, 1, 2, 3, 2]
    
    plt.scatter(a, b, s=300, edgecolors='y', marker='o', alpha = 0.5)
    plt.scatter(a, x, s=400, edgecolors='b', marker='4', alpha = 1)
    plt.legend(['b', 'x'], loc='best')
    plt.title('Scatter Plot Demo')
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    plt.grid(True)
    plt.savefig('scatplot.png')
    plt.show()


def main():
    # scatter_plot_01()
    # scatter_plot_02()
    # scatter_plot_03()
    pass
    
if __name__ == "__main__":
    main()
