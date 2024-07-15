import module
from module import addition
from module import subtraction
from module import multiplication, division

def import_method_01():
    retval = module.addition(10, 20)
    print(f"add retval :{retval}")

    retval = module.subtraction(10, 20)
    print(f"subtraction retval :{retval}")

    retval = module.multiplication(10, 20)
    print(f"multiplication retval :{retval}")

    retval = module.division(10, 20)
    print(f"divistion retval :{retval}")
    print()

def import_method_02():
    retval = addition(10, 20)
    print(f"add retval :{retval}")

    retval = subtraction(10, 20)
    print(f"subtraction retval :{retval}")

    retval = multiplication(10, 20)
    print(f"multiplication retval :{retval}")

    retval = division(10, 20)
    print(f"divistion retval :{retval}")
    print()
    
def main():
    import_method_01()
    import_method_02()
    
if __name__ == "__main__":
    main()
