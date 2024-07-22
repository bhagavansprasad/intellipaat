import numpy as np
import matplotlib.pyplot as plt

def line_plot_01(): # line plot line chart
    x = np.arange(0, 10, 0.1)
    y = (2*x) + 5
    
    plt.plot(x, y)
    plt.show()

def line_plot_02(): # Labelling x axis and y axis, adding title
    x = np.arange(0, 10, 0.1)
    y = (2*x) + 5
    
    plt.plot(x, y)
    plt.title("Line Plot Demo")
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    plt.show()

def line_plot_03(): # Line width line style opacity
    x = np.arange(0, 10, 0.2)
    y = (2*x) + 5
    
    plt.plot(x, y, linewidth = 2.0, linestyle = ":", color = 'r', alpha = 0.5, marker = 'o')
    plt.title("Line Plot Demo")
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    plt.legend(['Line1'], loc='best')
    plt.grid(True)
    plt.show()

def line_plot_04(): # Line width line style opacity
    x = np.arange(0, 10, 0.2)
    y = (2*x) + 5

    fig = plt.figure(figsize=(10, 5))
    plt.plot(x, y, linewidth = 2.0, linestyle = ":", color = 'r', alpha = 0.5, marker = 'o')
    plt.title("Line Plot Demo")
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    plt.legend(['Line1'], loc='best')
    plt.grid(True)
    plt.show()

def figure_two_line_plot_hori(): #horizontal
    x = np.arange(0, 10, 1)
    y1 = (2*x) + 5
    y2 = (3*x) + 10
    
    plt.subplot(2,1,1)
    plt.plot(x, y1)
    plt.title("Graph1")

    plt.subplot(2,1,2)
    plt.plot(x, y2)
    plt.title("Graph2")
    plt.show()

def figure_two_line_plot_verti(): # verticle
    x = np.arange(0, 10, 1)
    y1 = (2*x) + 5
    y2 = (3*x) + 10
    
    plt.subplot(1,2,1)
    plt.plot(x, y1)
    plt.title("Graph1")

    plt.subplot(1, 2, 2)
    plt.plot(x, y2)
    plt.title("Graph2")
    plt.show()

def main():
    # line_plot_01()
    # line_plot_02()
    # line_plot_03()
    # figure_two_line_plot_hori()
    # figure_two_line_plot_verti()
    pass
    
if __name__ == "__main__":
    main()
