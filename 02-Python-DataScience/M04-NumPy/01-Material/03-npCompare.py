import numpy as np

def element_compare():
    a = np.array([2, 4, 6])
    b = np.array([1, 5, 6])
    print(f"Equall a b :{np.equal(a, b)}")

    a = [2, 4, 6]
    b = [1, 5, 6]
    print(f"Equall a b :{np.equal(a, b)}")
    print(f"Array Equall a b :{np.array_equal(a, b)}")

    a = np.array(
        [
            [100, 200, 300],
            [5,   0,   15],
            [10,  20 , 30],
            [15,  90,  2],
        ])
    print(f"Equall       a b :{np.equal(a, a)}")
    print(f"Array Equall a b :{np.array_equal(a, a)}")

def aggregate_function():
    a = np.array([2, 4, 6])
    print(f"sum     a :{np.sum(a)}")
    print(f"minimum a :{np.min(a)}")
    print(f"mean    a :{np.mean(a)}")
    print(f"meadian a :{np.median(a)}")
    print(f"std deviation a :{np.std(a)}")

def np_broadcasting():
    a = np.array(
        [
            [100, 200, 300],
            [5,   0,   15],
            [10,  20 , 30],
            [15,  90,  2],
        ])

    b = np.array([100, 200, 300])
    print(f"-->a   :\n{a}")
    print(f"-->b   :\n{b}")
    print(f"-->a+b :\n{a+b}")
    
    b = np.array([[100, 200, 300]])
    print(f"-->b   :\n{b}")
    print(f"-->a+b :\n{a+b}")
    

def main():
    # element_compare()
    # aggregate_function()
    np_broadcasting()

    pass

if __name__ == "__main__":
    main()
