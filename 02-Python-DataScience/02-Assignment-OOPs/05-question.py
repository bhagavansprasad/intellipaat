ddata = {
    "slow" : 2,
    "medium" : 9,
    "fast" : 22,
}

def main():
    car_0 = {'x_position': 10, 'y_position': 72, 'speed': 'slow'}
    car_1 = {'x_position': 10, 'y_position': 72, 'speed': 'medium'}
    car_2 = {'x_position': 10, 'y_position': 72, 'speed': 'fast'}

    print("Before increment....")    
    print(f"car_0 :{car_0}")
    print(f"car_1 :{car_1}")
    print(f"car_2 :{car_2}")
    print()
    
    car_0['x_position'] += ddata[car_0['speed']]
    car_1['x_position'] += ddata[car_1['speed']]
    car_2['x_position'] += ddata[car_2['speed']]

    print("After increment....")    
    print(f"car_0 :{car_0}")
    print(f"car_1 :{car_1}")
    print(f"car_2 :{car_2}")


if __name__ == "__main__":
    main()
