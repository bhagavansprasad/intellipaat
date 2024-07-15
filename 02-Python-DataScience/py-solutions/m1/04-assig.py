def is_prime(number):
    if number < 1:
        return False
    
    if number == 2:
        return True
    
    if number % 2 == 0:
        return False
    
    for i in range(3, number-1, 2):
        if number % i == 0: 
            return False
    
    return True

num_list = [2, 5, 7, 8, 11, 15, 23, 29]

def main():
    for i in num_list:
        if (is_prime(i)):
            print(i)
    
if __name__ == "__main__":
    main()
    