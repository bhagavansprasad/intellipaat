import numpy as np

def question_01(tp):
    a = np.full(tp, 5)
    print (f"a :\n{a}")

def sum_arrays(*arrays): # np array adding adding arrays
    summed_array = np.sum(arrays, axis=0)
    return summed_array

def question_02(): # creating 2d np array
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])
    c = np.array([[9, 10], [11, 12]])

    s = sum_arrays(a, b, c)
    print (f"s :\n{s}")


def get_left_sub_matrix(a, m, n):
    return a[0:m+1, 0:n+1]

def question_03():
    a = np.random.randint(50, 100, size = (8, 8))
    print (f"a :\n{a}")

    m=3; n=3
    b = get_left_sub_matrix(a, m, n)
    print (f"m :{m}, n :{n} of a :\n{b}")
    
    m=2; n=5
    b = get_left_sub_matrix(a, m, n)
    print (f"m :{m}, n :{n} of a :\n{b}")

def get_bottom_right_sub_matrix(a, m, n):
    return a[-m:, -n:]

def question_04():
    a = np.random.randint(50, 100, size = (8, 8))
    print (f"a :\n{a}")

    m=2; n=2
    b = get_bottom_right_sub_matrix(a, m, n)
    print (f"m :{m}, n :{n} of a :\n{b}")

    m=3; n=3
    b = get_bottom_right_sub_matrix(a, m, n)
    print (f"m :{m}, n :{n} of a :\n{b}")
    
    m=2; n=5
    b = get_bottom_right_sub_matrix(a, m, n)
    print (f"m :{m}, n :{n} of a :\n{b}")
    
def get_mean_n_std_deviation(a):
    return {'mean': np.mean(a), 'std_dev': np.std(a)}
    
def question_05():
    a = np.random.randint(50, 100, size = 10)
    print (f"a :\n{a}")
    
    d = get_mean_n_std_deviation(a)
    print (f"retval :{d}")

def main():
    question_01((3, 3))
    question_02()
    question_03()
    question_04()
    question_05()
    
if __name__ == "__main__":
    main()
    