class Triangle:
    angle1 = -1
    angle2 = -1
    angle3 = -1
    
    def __init__(self, angle1, angle2, angle3) -> None:
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
        
    def check_angles(self):
        if (self.angle1 + self.angle2 + self.angle3 == 180):
            return True
        else:
            return False
    
    def get_traingle_type(self):
        max_angle = max(self.angle1, self.angle2, self.angle3)
        if (max_angle > 90):
            return "Obtuse Angle"
        elif (max_angle < 90):
            return "Acute Angle"
        else:
            return "Right Angle"

class isosceles_triangle(Triangle):
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
        
        if ((angles_list[0] == angles_list[1] or angles_list[1] == angles_list[2]) and 
            (sides_list[0] == sides_list[1] or sides_list[1] == sides_list[2])): 
            return True
        else:
            return False
            
     
class right_triangle(Triangle):
    side1 = -1
    side2 = -1
    side3 = -1
    
    def __init__(self, angle1, angle2, angle3, side1, side2, side3) -> None:
        super().__init__(angle1, angle2, angle3)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def is_right_triangle(self):
        if (90 in [self.angle1, self.angle2, self.angle3]):
            return True
        else:
            return False
            
class equilateral_triangle(Triangle):
    side1 = -1
    side2 = -1
    side3 = -1
    
    def __init__(self, angle1, angle2, angle3, side1, side2, side3) -> None:
        super().__init__(angle1, angle2, angle3)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def is_equilateral_triangle(self):
        angles_list = [self.angle1, self.angle2, self.angle3]
        sides_list = [self.side1, self.side2, self.side3]
        
        if ((angles_list[0] == angles_list[1] and angles_list[1] == angles_list[2]) and 
            (sides_list[0] == sides_list[1] and sides_list[1] == sides_list[2])): 
            return True
        else:
            return False
        
def main():
    tobj1 = Triangle(60, 80, 40)
    print(f"Is total angle is 180 :{tobj1.check_angles()}")
    
    tobj2 = Triangle(60, 60, 40)
    print(f"Is total angle is 180 :{tobj2.check_angles()}")
    print(f"Get angle type        :{tobj2.get_traingle_type()}")

    tobj3 = Triangle(90, 60, 40)
    print(f"Is total angle is 180 :{tobj3.check_angles()}")
    print(f"Get angle type        :{tobj3.get_traingle_type()}")

    tobj4 = Triangle(120, 60, 40)
    print(f"Is total angle is 180 :{tobj4.check_angles()}")
    print(f"Get angle type        :{tobj4.get_traingle_type()}")
    
    iobj = isosceles_triangle(50, 50, 80, 5, 5, 10)
    print(f"is iobj is is_isosceles_triangle :{iobj.is_isosceles_triangle()}")
    
    robj = right_triangle(90, 50, 40, 5, 5, 10)
    print(f"is robj is right_triangle :{robj.is_right_triangle()}")

    eobj = equilateral_triangle(60, 60, 60, 5, 5, 5)
    print(f"is eobj is equilateral_triangle :{eobj.is_equilateral_triangle()}")

if __name__ == "__main__":
    main()
