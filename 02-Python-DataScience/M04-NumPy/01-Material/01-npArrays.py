import numpy as np

def oned_array():
    a = np.array([10, 20 , 30])
    print(a)
    print(type(a))
    
    print(list(a))

def twod_array():
    a = np.array(
        [
            [100, 200, 300],
            [5, 0, 15],
            [10, 20 , 30]
        ])
        
    print(a)
    print(type(a))
    
    print(list(a))
    
    for tlist in list(a):
        print(list(tlist))

def init_2d_array():
    a = np.array([10, 20 , 30])
    b = np.array(
        [
            [100, 200, 300],
            [5, 0, 15],
            [10, 20 , 30]
        ])
    c = np.zeros((3, 4))
    
    print(f"type(a) :{type(a)}")
    print(f"     a  :{a}")
    print(f"list(a) :{list(a)}")

    print(f"type(b) :{type(b)}")
    print(f"     b  :{b}")
    print(f"list(b) :{list(b)}")

    print(f"type(c) :{type(c)}")
    print(f"     c  :{c}")
    print(f"list(c) :{list(c)}")
    print()

    return

def arange_01():
    a = np.arange(1, 10, 2)
    print(f"type(a) :{a.dtype}")
    print(f"     a :{a}")

    a = np.arange(10, 30, 5)
    print(f"type(a) :{a.dtype}")
    print(f"     a  :{a}")

    a = np.arange(1, 11, dtype=float)
    print(f"type(a) :{a.dtype}")
    print(f"     a  :{a}")

    a = np.arange(1, 3, dtype=bool)
    print(f"type(a) :{a.dtype}")
    print(f"     a  :{a}")

def arrange_numbers():
    a = np.linspace(5, 10, 10)    
    print(f"type(a) :{type(a)}")
    print(f"     a  :{a}")

    a = np.linspace(0, 10, 6)    
    print(f"type(a) :{type(a)}")
    print(f"     a  :{a}")

def full_01():
    a = np.full((2, 2), 5)    
    print(f"     a  :{a}")

    a = np.full((7, 7), 0)    
    print(f"-->a  :\n{a}")

    a = np.full((7, 7), "Hi")
    print(f"-->a  :\n{a}")

    print()

def random_fill():
    a = np.random.random((2, 2))    
    print(f"     a  :{a}")

    a = np.random.random((3, 4))    
    print(f"-->a  :\n{a}")

    print()

def random_fill():
    a = np.random.random((2, 2))    
    print(f"     a  :{a}")

    a = np.random.random((3, 4))    
    print(f"-->a  :\n{a}")
    
    print()

def inspect_array():
    a = np.array(
        [
            [100, 200, 300],
            [5,   0,   15],
            [10,  20 , 30],
            [15,  90,  2],
        ])
        
    print(f"-->a   :\n{a}")
    print(f"a size :{a.shape}")

def resize_array():
    a = np.array(
        [
            [100, 200, 300],
            [5,   0,   15],
            [10,  20 , 30],
            [15,  90,  2],
        ])
        
    print(f"-->a   :\n{a}")
    print(f"a size :{a.shape}")
    print(f"a ndim :{a.ndim}")
    
    print(f"After shaping to 2, 3")
    a.shape = (6, 2)
    print(f"-->a   :\n{a}")
    print(f"a size :{a.shape}")

    print(f"Change back to original 4, 3")
    a.shape = (4, 3)
    print(f"-->a   :\n{a}")
    print(f"a size :{a.shape}")
    
    print(f"After shaping to 12, 1")
    a.shape = (12, 1)
    print(f"-->a   :\n{a}")
    print(f"a size :{a.shape}")

    print(f"After shaping to 1, 12")
    a.shape = (1, 12)
    print(f"-->a   :\n{a}")
    print(f"a size :{a.shape}")
    
def get_dimention():
    a = np.arange(24)

    print(f"-->a   :\n{a}")
    print(f"a ndim :{a.ndim}")

def get_dimention():
    a = np.arange(1, 25)

    print(f"-->a   :\n{a}")
    print(f"a ndim :{a.ndim}")
    
    a.shape = (6, 4)
    print(f"-->a   :\n{a}")
    print(f"a size :{a.shape}")
    print(f"a ndim :{a.ndim}")

    a.shape = (3, 4, 2)
    print(f"-->a   :\n{a}")
    print(f"a size :{a.shape}")
    print(f"a ndim :{a.ndim}")

    a.shape = (2, 1, 12)
    print(f"-->a   :\n{a}")
    print(f"a size :{a.shape}")
    print(f"a ndim :{a.ndim}")

def get_size():
    a = np.array(
        [
            [100, 200, 300],
            [5,   0,   15],
            [10,  20 , 30],
            [15,  90,  2],
        ])
        
    print(f"-->a   :\n{a}")
    print(f"a size :{a.shape}")
    print(f"a ndim :{a.ndim}")
    print(f"a size :{a.size}")

def np_help():
    a = np.array(
        [
            [100, 200, 300],
            [5,   0,   15],
            [10,  20 , 30],
            [15,  90,  2],
        ])

    
def main():
    # oned_array()
    # twod_array()
    # init_2d_array()
    # arange_01()
    # arrange_numbers()
    # full_01()
    # random_fill()
    # inspect_array()
    # resize_array()
    # get_dimention()
    # get_size()
    # np_help()
    pass

if __name__ == "__main__":
    main()
    
