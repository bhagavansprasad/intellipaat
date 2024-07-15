import numpy as np

def np_sum():
    a = np.arange(1, 10)
    print(f"sum :{np.sum(a)}")
    
    a = np.array(
        [
            [10,  20,  30],
            [5,   10,  15],
            [10,  20 , 30],
            [20,  10,  2],
        ])

    print(f"-->a   :\n{a}")
    print(f"sum axis 0 (col):{np.sum(a, axis = 0)}")
    print(f"sum axis 1 (row):{np.sum(a, axis = 1)}")
    print(f"sum No axis     :{np.sum(a)}")

def np_other_math_operations_01():
    a = np.arange(1, 10)
    print(f"subtract :{np.subtract(10, 20)}")
    
    a = np.array(
        [
            [10,  20,  30],
            [5,   10,  15],
            [10,  20 , 30],
            [20,  10,  2],
        ])

    print(f"-->a   :\n{a}")
    print(f"multi :{np.multiply(a, a)}")

    a = np.array(
        [
            [10,  20,  30],
            [5,   10,  15],
            [10,  20 , 30],
            [20,  10,  2],
        ])

    b = np.array(
        [
            [10,  20,  30],
            [5,   10,  15],
            [10,  20 , 30],
            [20,  10,  2],
        ])
    
    retval = np.divide(a, b)
    print(f"retval :{retval}")

def np_other_math_operations_02():
    a = np.array(
        [
            [10,  20,  30],
            [5,   10,  15],
            [10,  20 , 30],
            [20,  10,  2],
        ])

    print(f"exponent :{np.exp(a)}")
    print(f"sqrt     :{np.sqrt(a)}")
    print(f"sin      :{np.sin(a)}")
    print(f"log      :{np.log(a)}")
    print(f"log      :{np.log(a)}")

        
def main():
    # np_sum()
    # np_other_math_operations_01()
    np_other_math_operations_02()

if __name__ == "__main__":
    main()
    
