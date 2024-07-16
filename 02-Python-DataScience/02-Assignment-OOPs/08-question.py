def main():
    dlist = list(range(1, 51))
    print(f"dlist :{dlist}")
    
    lf = lambda x: x*x
    
    lsquares = list(map(lf, dlist))
    print(f"Squares :{lsquares}")

if __name__ == "__main__":
    main()
