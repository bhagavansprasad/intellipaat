import numpy as np

def np_broadcasting():
    a = np.array([2, 4, 6])
    b = np.array([1, 5, 6])

    c = np.concatenate((a, b))
    print(f"-->a   :\n{a}")
    print(f"-->b   :\n{b}")

    print(f"conatenate a b :\n{c}")
    print(f"vstack       a b :\n{np.vstack((a,b))}")
    print(f"column_stack a b :\n{np.column_stack((a,b))}")

def splitting_examples():
    a = np.arange(16).reshape(4, 4)
    print(f"-->a   :\n{a}")
    
    b = np.hsplit(a, 2)
    print(f"-->split a 2  :\n{b}")
    
    for array in b:
        print(array)
    
    b = np.hsplit(a, np.array([3]))
    print(f"-->split a 3  :\n{b}")

    b = np.hsplit(a, np.array([2, 3]))
    print(f"-->split a 3  :\n{b}")

def main():
    # element_compare()
    # aggregate_function()
    # np_broadcasting()
    # splitting_examples()
    pass

if __name__ == "__main__":
    main()
    