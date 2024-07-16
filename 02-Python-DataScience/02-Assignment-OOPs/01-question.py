import datetime

class Employee:
    EmployeeID = 0
    Gender = ""
    Salary = 0
    PerformanceRating = 0

    def __init__(self, eid, gender, salary, rating):
        self.EmployeeID = eid
        self.Gender = gender
        self.Salary = salary
        self.PerformanceRating = rating
        
        
class JoiningDetail:
    DateOfJoining = ""
    
    def __init__(self, doj) -> None:
        self.DateOfJoining = doj
        
    def getDoJ(self):
        return self.DateOfJoining

class Information(Employee, JoiningDetail):
    
    def __init__(self, eid, gender, salary, rating, doj):
        Employee.__init__(self, eid, gender, salary, rating)
        JoiningDetail.__init__(self, doj)
        
    def readData(self):
        return self.EmployeeID, self.Gender, self.Salary, self.PerformanceRating, self.getDoJ()
        
    
def main():
    obj1 = Information(10, "Male", 1000, 5, datetime.datetime.now())
    obj2 = Information(11, "Male", 2000, 4, datetime.datetime.now())
    obj3 = Information(12, "Female", 3000, 4, datetime.datetime.now())
    
    print(obj1.readData())
    print(obj2.readData())
    print(obj3.readData())

if __name__ == "__main__":
    main()