import numpy as np
import matplotlib.pyplot as plt

def histogram_plot_01(): 
    numbers = [10, 12, 16,19,11,20,26,28,30,38,35,34,60,68,64,62,70,78,75,79,85,94,95]
    plt.hist(numbers, bins = [0, 20, 30,40,60,80,100])
    plt.show()

def histogram_plot_02(): 
    numbers = [10, 12, 16,19,11,20,26,28,30,38,35,34,60,68,64,62,70,78,75,79,85,94,95]
    plt.hist(numbers, bins = [0, 20, 30,40,60,80,100])
    plt.title('Histogram Demo')
    plt.xlabel("Range of values")
    plt.ylabel("Frequence of values ")
    
    plt.show()

def histogram_plot_03(): 
    numbers = [10, 12, 16,19,11,20,26,28,30,38,35,34,60,68,64,62,70,78,75,79,85,94,95]
    plt.hist(numbers, bins = [0, 20, 30,40,60,80,100], edgecolor = '#000000', color = "#FF2331")
    plt.title('Histogram Demo')
    plt.xlabel("Range of values")
    plt.ylabel("Frequence of values ")
    plt.grid(True)
    plt.show()

def main():
    # histogram_plot_01()
    # histogram_plot_02()
    # histogram_plot_03()
    pass
    
if __name__ == "__main__":
    main()
