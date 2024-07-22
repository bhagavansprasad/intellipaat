import numpy as np
import matplotlib.pyplot as plt

def bar_plot_01(): # line plot line chart
    data = {'apples' : 20, 'Mangoes' : 15, 'Lemon': 30, 'Oranges' : 10}
    
    names = list(data.keys())
    values  = list(data.values())
    
    fig = plt.figure(figsize = (10, 5))
    plt.bar(names, values)
    plt.show()

def bar_plot_verticle(): 
    data = {'apples' : 20, 'Mangoes' : 15, 'Lemon': 30, 'Oranges' : 10}
    
    names = list(data.keys())
    values  = list(data.values())
    
    fig = plt.figure(figsize = (10, 5))
    plt.bar(names, values, color = 'orange')
    plt.title("Bar Graph Demo")
    plt.xlabel("Fruits")
    plt.ylabel("Quntity")
    plt.show()


def bar_plot_horizontol(): 
    data = {'apples' : 20, 'Mangoes' : 15, 'Lemon': 30, 'Oranges' : 10}
    
    names = list(data.keys())
    values  = list(data.values())
    
    fig = plt.figure(figsize = (10, 5))
    plt.barh(names, values, color = 'orange')
    plt.title("Bar Graph Demo")
    plt.xlabel("Fruits")
    plt.ylabel("Quntity")
    plt.show()

def main():
    # bar_plot_01()
    # bar_plot_verticle()
    bar_plot_horizontol()
    pass
    
if __name__ == "__main__":
    main()
