class student:
    def fun1(self):
        tstr = "How are you"
        return tstr
    
    def fun2(self, tstr):
        print(f"tstr :{tstr}")
        
def factor(n):
    f = 1
    
    for i in range (2, n+1):
        f = f * i
        
    return f

def check_string(str):
    if ('s' in str):
        print(f"The string is containing the letter 's'")
    else:
        print(f"The string DOESNOT containing the letter 's'")

def define_lambda_function():
    double_num = lambda x: x*x
    print(double_num(5))

def main():
    n = 5
    factval = factor(n)
    print(f"factorial value of {n} is {factval}")
    print()

    tstr = "Aura Networks"
    check_string(tstr)
    print()

    tstr = "Intellipat"
    check_string(tstr)
    print()
        
    sobj = student()
    retval = sobj.fun1()
    sobj.fun2(retval)
   
    define_lambda_function()
if __name__ == "__main__":
    main()
    