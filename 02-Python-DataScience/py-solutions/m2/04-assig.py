class parent_Class():
    num = 0
    
class child_Class(parent_Class):
    pass

def question_01():
    cobj = child_Class()
    cobj.num = 10
    print(f"parent class glocal value num :{cobj.num}")
    print()

###############################################################

class A():
    name = None
    age = 0
    
    def __init__(self) -> None:
        name = None
        age = 0
        
    def details(self):
        return self.name

class B():
    name = None
    id = 0
    
    def __init__(self) -> None:
        name = None
        id = 0
        
    def details(self):
        return self.name

class C(A, B):
    name = None
    id = 0
    
    def __init__(self) -> None:
        A.__init__(self)
        
    def get_details(self):
        return self.name

def question_02():
    Cobj = C()
    retval = Cobj.get_details()
    print(f"retval :{retval}")
    print()

###############################################################

class Sub1():
    def first(self):
        print('This is the first function from Sub 1 class')

class Sub2():
    def second(self):
        print('This is the second function from Sub 2 class')

class Super(Sub1, Sub2):
    def final(self):
        print('This is the final method from the super class')

def question_03():
    sobj = Super()
    sobj.first()
    sobj.second()
    sobj.final()
    print()

###############################################################

class Parent():
    def fun1(self):
        print('This is the message from the fun1')

class Child1():
    def fun2(self):
        print('This is the message from the fun2')

class Child2(Parent):
    def fun3(self):
        print('This is the message from the fun3')

def question_04():
    chld2 = Child2()
    chld2.fun1()
    print()

###############################################################

class Parent():
    def fun1(self):
        print('This is the message from the fun1')

class Child():
    def fun2(self):
        print('This is the message from the fun2')

class Hybrid(Parent, Child):
    def fun3(self):
        print('This is the message from the fun3')

def question_05():
    hyb = Hybrid()
    hyb.fun1()
    hyb.fun2()
    hyb.fun3()
    print()
###############################################################

def main():
    question_01()
    question_02()
    question_03()
    question_04()
    question_05()
    
if __name__ == "__main__":
    main()
