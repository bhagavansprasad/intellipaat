class Vehicle:
    fare = 0

    def __init__(self, Fare):
        self.fare = Fare

    def get_fare(self):
        return self.fare

def main():
    bus = Vehicle(10)
    car = Vehicle(20)
    train = Vehicle(30)
    truck = Vehicle(40)
    ship = Vehicle(50)
    
    TotalFare = bus.get_fare() + car.get_fare() + train.get_fare() + truck.get_fare() + ship.get_fare()
    print (f"TotalFare :{TotalFare}")

if __name__ == "__main__":
    main()
    
    
    
