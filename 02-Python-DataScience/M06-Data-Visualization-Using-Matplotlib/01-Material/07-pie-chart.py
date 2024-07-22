import numpy as np
import matplotlib.pyplot as plt

def pie_chart_01(): 
    labels = ['Dog', 'Cat', 'Wolf', 'Lion']
    sizes = [50, 45, 60, 80]
    
    plt.pie(sizes, labels = labels, autopct='%1.1f%%', shadow=True, startangle = 90)
    plt.title("Pie chart Demo")
    plt.show()

def doughnut_chart_01(): 
    group_names = ["GroupA", "GroupB", "GroupC"]
    group_size = [20, 30, 50]
    size_center = [5]

    pie1 = plt.pie(group_size, labels= group_names, radius = 1.5)
    pie2 = plt.pie(size_center, radius = 1.0, colors='w')
    plt.show()

def main():
    # pie_chart_01()
    doughnut_chart_01()
    pass
    
if __name__ == "__main__":
    main()
