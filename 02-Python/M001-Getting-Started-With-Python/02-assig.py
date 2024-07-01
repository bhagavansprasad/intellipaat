def compare_numbers(a, b, c):
    if (a > b):
        if (a > c):
            print(f"A: {a} is BIG")
        else:
            print(f"C: {c} is BIG")
    elif (b > c):
        print(f"B: {b} is BIG")
    elif (c > b):
        print(f"C: {c} is BIG")

def main():
    compare_numbers(10, 20, 30)
    compare_numbers(10, 30, 20)
    compare_numbers(30, 20, 10)
    
if __name__ == "__main__":
    main()
    