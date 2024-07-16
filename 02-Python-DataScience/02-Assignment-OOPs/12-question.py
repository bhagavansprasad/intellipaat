class Triangle:
    angle1 = -1
    angle2 = -1
    angle3 = -1
    
    def __init__(self, angle1, angle2, angle3) -> None:
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
        

class isosceles_right_triangle(Triangle):
    side1 = -1
    side2 = -1
    side3 = -1
    
    def __init__(self, angle1, angle2, angle3, side1, side2, side3) -> None:
        super().__init__(angle1, angle2, angle3)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def is_isosceles_triangle(self):
        angles_list = [self.angle1, self.angle2, self.angle3]
        angles_list.sort(reverse=True)

        sides_list = [self.side1, self.side2, self.side3]
        sides_list.sort(reverse=True)
        
        if (90 in angles_list and 
            (sides_list[0] == sides_list[1] or sides_list[1] == sides_list[2])): 
            return True
        else:
            return False
        
def main():
    iobj = isosceles_right_triangle(90, 45, 45, 3, 3, 5)
    print(f"is iobj is is_isosceles_right_triangle :{iobj.is_isosceles_triangle()}")
    

if __name__ == "__main__":
    main()
