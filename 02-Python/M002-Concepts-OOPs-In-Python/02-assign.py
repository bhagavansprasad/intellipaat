class Super:
    def fun1(self):
        print("This is function 1 in the Super class")
        
    def Hello(self, t1):
        print(f"This function is only having 1 argument")

class Modified_Super(Super):
    def fun1(self):
        print("This is function 1 in the Modified Super class")

    def fun2(self):
        print("This is the 2 nd function from the Modified Super class' in the print statement")

    def Hello(self, t1):
        print(f"This function is only having 1 argument")

    def Hello(self, t1, t2):
        print(f"This function is having 2 arguments")

    def sum(self, *args):
        sum = 0
        for i in args:
            sum += i
        return sum
    
class Encapsulation():
    originalValue = 0
    
    def __init__(self):
        self.originalValue = 10
    
    def value(self):
        return self.originalValue

    def setValue(self, val):
        self.originalValue = val

def main():
    sobjb = Super()
    sobjb.fun1()

    sobjd = Modified_Super()
    sobjd.fun1()
    sobjd.fun2()
    
    # sobjd.Hello("hi")
    sobjd.Hello("Hi", "Bye")
   
    retval = sobjd.sum(10, 20, 30)
    print(f"retval :{retval}")

    retval = sobjd.sum(10, 20, 30, 40, 50)
    print(f"retval :{retval}")
   
    eobj = Encapsulation()
    retval = eobj.value()
    print(f"retval :{retval}")

    eobj.setValue(100)
    retval = eobj.value()
    print(f"retval :{retval}")
    
if __name__ == "__main__":
    main()
    