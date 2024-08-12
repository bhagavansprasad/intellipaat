import pandas as pd
import numpy as np
import scipy.stats as st

def get_standadrd_deviation():
    tlist = [42, 61, 39, 70, 8, 30, 52, 28, 95, 86, 35, 77, 80, 86, 1, 84, 90, 57, 45, 6, 1, 56, 60, 83, 24, 63, 93, 59, 92, 53]
    print(f"Values :{tlist}")

    std = np.std(tlist)
    print(f'stadard deviation :{std}')

def get_variance():    
    tlist = [42, 61, 39, 70, 8, 30, 52, 28, 95, 86, 35, 77, 80, 86, 1, 84, 90, 57, 45, 6, 1, 56, 60, 83, 24, 63, 93, 59, 92, 53]
    print(f"Values :{tlist}")

    var =  np.var(tlist)
    print(f'variation :{var}')
    
def interquartile_range():
    tlist = [17, 27, 80, 39, 72, 95, 52, 85, 8, 64, 36, 15, 62, 76, 66, 67, 59, 92]
    
    #              Q1                           Q2
    # [ 8 15 17 27 36 39 52 59 62 | 64 66 67 72 76 80 85 92 95]
    #  Median = (62+64)/2 = 63
    # Q1 = 36
    # Q2 = 76
    # IQR = 76 - 36 = 40
    # tlist.sort()
    nparr = np.array(tlist) # max-value - min-value
    range_of_array = np.ptp(nparr)
    median = nparr.mean()
    q1 = np.percentile(nparr, 25)
    q3 = np.percentile(nparr, 75)
    print(q1)
    print(q3)
    iqr = q3 - q1
    print(f"range :{range_of_array}")
    print(f"mean :{median}")
    print(f"q1   :{q1}")
    print(f"q3   :{q3}")
    print(f"iqr  :{iqr}")
    
def distribution():
    # mean 56   - sum-of-all/count
    # median 63 - Middle value 
    # mode 65   - Most frequent
    values = [65, 65, 65, 63, 63, 50, 55, 70, 75, 40]
    
    # Positively Skewed (Right Skewed): The mean is greater than the median, and 
    #   the median is greater than the mode. 
    #   This means the tail on the right side of the distribution is longer or fatter.
    #  Mode > Median > Mean

    # Negatively Skewed (Left Skewed): The mean is less than the median, 
    #   and the median is less than the mode. 
    #   This means the tail on the left side of the distribution is longer or fatter.
    #  Mean > Median > Mode
    pass

def mean_medin_mode(data):
    mean = np.mean(data)
    median = np.median(data)
    mode = st.mode(data)[0]
    
    return mean, median, mode
    
def get_mean_medin_mode():

    #    
    a = [50, 55, 60, 62, 63, 64, 65, 65, 66, 68, 70, 72, 75, 80, 85, 90, 95, 100]
    # mean :71.38888888888889, median :67.0, mode :65
    # Positively Skewed (Right Skewed)
    # Mean > Median > Mode
    #  71     67      65
    
    b = [150, 155, 160, 162, 163, 164, 165, 165, 166, 168, 170, 172, 175, 180, 185, 190, 195, 50]
    # mean :163.05555555555554, median :165.5, mode :165
    # Mean < Median < Mode
    #  163    165.5   165
    
    mean, median, mode = mean_medin_mode(a)
    print(f"a :{a}\nmean :{mean}, median :{median}, mode :{mode}")

    mean, median, mode = mean_medin_mode(b)
    print(f"b :{b}\nmean :{mean}, median :{median}, mode :{mode}")

def main():
    # get_standadrd_deviation()
    # get_variance()
    # interquartile_range()
    get_mean_medin_mode()

if (__name__ == '__main__'):
    main()

