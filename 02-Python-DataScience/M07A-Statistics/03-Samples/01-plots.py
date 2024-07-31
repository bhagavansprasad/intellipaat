
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



def main():
    sample_01()
    
if (__name__ == '__main__'):
    main()

