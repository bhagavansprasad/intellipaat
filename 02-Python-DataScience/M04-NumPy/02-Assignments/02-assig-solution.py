import numpy as np

def question_01():
    npar = np.array(np.arange(2, 11)).reshape(3,3)
    print (f"npar :\n{npar}")

def question_02():
    npari = np.arange(1, 9)
    print (f"npari :\n{npari}")
    
    nparf = np.array(npari, dtype=float)
    print (f"nparf :\n{nparf}")

def question_03():
    npar = np.arange(10, 31, 10)
    npar = np.append(npar, [50, 60, 70, 80, 90])
    print (f"npar      :\n{npar}")
    

def question_04():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    print (f"a & type :{a}, {type(a)}")
    print (f"b & type :{b}, {type(b)}")

    c = np.add(a, b)
    print (f"c & type :{c}, {type(c)}")
    
    a = np.arange(1, 10)
    b = np.arange(10, 19)
    print (f"a & type :{a}, {type(a)}")
    print (f"b & type :{b}, {type(b)}")
    
    c = np.add(a, b)
    print (f"c & type :{c}, {type(c)}")
    
def question_05():
    a = np.array(np.arange(10, 100, 10)).reshape(3,3)
    print (f"a :\n{a}")
    print (f"a[0]      :{a[0]}")
    print (f"a[-1][-1] :{a[-1][-1]}")

def main():
    question_01()
    question_02()
    question_03()
    question_04()
    question_05()
    
if __name__ == "__main__":
    main()
    