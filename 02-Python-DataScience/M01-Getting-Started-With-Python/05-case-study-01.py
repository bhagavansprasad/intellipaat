def get_squares(n):
    squares =  [i*i for i in range(1, n+1)]
    print(squares)
    print()

def is_leap_year(yy):
    if (((yy % 4 == 0) and (yy % 100 != 0)) or (yy % 400 == 0)):
        print (f"{yy} is a Leap")
    else:
        print (f"{yy} is NOT a Leap")
       
def get_evens(tlist):
    retvals = []
    for i in tlist:
        if (i %2 == 0):
            retvals.append(i)
    
    return retvals    

def is_exists(a, b):
    for i in a:
        if i in b:
            print(i, end = " ")
    print()

num_list = [2, 4, 7, 10, 11, 24, 23, 29]
num_list2 = [2, 7, 10, 23, 29]

def main():
    n = 10

    get_squares(n)

    is_leap_year(2024)
    is_leap_year(2020)
    is_leap_year(2100)
    is_leap_year(2400)
    print()

    even_list = get_evens(num_list)
    print(even_list)
    print()
    
    is_exists(num_list, num_list2)
    print()
    
if __name__ == "__main__":
    main()
    