import numpy as np
import matplotlib.pyplot as plt

def violin_plot_01(): 
    total = [20, 4, 1, 30, 20, 10, 20, 70, 30, 10]
    order = [10, 2, 1, 15, 17, 2, 30, 44, 2, 1]
    discount = [30, 10, 20, 5, 10, 20, 50, 60, 20, 45]
    
    data = list([total, order, discount])

    plt.title('Blox Plot Demo')
    plt.grid(True)
    plt.violinplot(data, showmeans = True, showmedians=True)
            
    plt.show()

def main():
    violin_plot_01()
    pass
    
if __name__ == "__main__":
    main()
