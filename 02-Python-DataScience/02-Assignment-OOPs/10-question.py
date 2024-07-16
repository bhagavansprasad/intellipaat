class Triangle:
    number_of_side = -1 #class variable
    
    def __init__(self) -> None:
        Triangle.number_of_side = 3 #class variable
    
    def display(self):
        print(f"number_of_side :{self.number_of_side}")

def main():
    tobj = Triangle()
    tobj.display()
    

if __name__ == "__main__":
    main()
