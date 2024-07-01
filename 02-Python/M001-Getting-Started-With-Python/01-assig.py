def compare_numbers(a, b):
    if (a > b):
        print(f"A: {a} is BIG. B: {b}")
    elif (b > a):
        print(f"B: {b} is BIG. A:{a}")
    else:
        print(f"A & B Are SAME. A: {a}, B: {b}")

def main():
    compare_numbers(10, 20)
    compare_numbers(20, 10)
    compare_numbers(10, 10)
    compare_numbers(0, 0)
    
if __name__ == "__main__":
    main()
    