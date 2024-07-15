import numpy as np

def slice_n_dice():
    a = np.arange(1, 10).reshape(3, 3)
    print(f"-->a   :\n{a}")
    
    print()
    print(f"a[0]       :\n{a[0]}")
    print(f"a[:1]      :\n{a[:1]}")
    print(f"a[:1, 1:]  :\n{a[:1, 1:]}")
    print(f"a[0:2, 1:] :\n{a[0:2:, 1:]}")
    print(f"a[1:, 1:]  :\n{a[1:, 1:]}")
    

def main():
    slice_n_dice()
    pass

if __name__ == "__main__":
    main()
