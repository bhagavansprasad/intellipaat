class Employee():
    name = ""
    salary = 0
    
    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = salary
        
    def __str__(self):
        return f"Name: {self.name}, Salary: {self.salary}"    

def question_01():
    eobj = Employee("Bhagavan", 1000)
    print(eobj)
########################################################
class Calculator():
    def addition(self, a, b):
        return a+b

    def subtraction(self, a, b):
        return a-b

    def multiplication(self, a, b):
        return a*b

    def division(self, a, b):
        return a/b

def execute(cmd, a, b):
    cobj = Calculator()
    cmds = {
        "add": cobj.addition,
        "sub": cobj.subtraction,
        "mul": cobj.multiplication,
        "div": cobj.division
    }
    
    try:
        retval = cmds[cmd](a, b)
        print(f"Operation {cmd}, a :{a}, b :{b}, retval :{retval}")
    except:
        print(f"Invalid operation :{cmd}")

def question_03():
    execute("add", 10, 20)
    execute("sub", 10, 20)
    execute("mul", 10, 20)
    execute("div", 10, 20)

########################################################
def main():
    question_01()
    question_03()

if __name__ == "__main__":
    main()
