class Triangle:
    angle1 = -1
    angle2 = -1
    angle3 = -1
    
    def __init__(self, angle1, angle2, angle3) -> None:
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
    
def main():
    tobj = Triangle(5, 10, 15)
    

if __name__ == "__main__":
    main()
