import numpy as np
import sys
import time

def list_Vs_nparray():
    l = list(range(1000))
    a = np.arange(1000)
    
    print(f"l size :{sys.getsizeof(l)*len(l)}")
    print(f"l size :{a.size * a.itemsize}")

    a = 10
    print(f"a size :{sys.getsizeof(a)}")

    a = "Aura"
    print(f"a size :{sys.getsizeof(a)}")
    

def check_list_time():
    t1 = time.time()
    a = range(10000)
    b = range(10000)
    
    c = [a[i] + b[i] for i in range(len(a))]
    return time.time() - t1

def check_nparray_time():
    t1 = time.time()
    a = np.arange(10000)
    b = np.arange(10000)
    
    c = a + b

    return time.time() - t1
        
    
def main():
    # list_Vs_nparray()
    retval1 = check_list_time()
    print(f"list access time    :{retval1}")

    retval2 = check_nparray_time()
    print(f"nparray access time :{retval2}")
    
    print(retval1/retval2)
    
    pass

if __name__ == "__main__":
    main()
