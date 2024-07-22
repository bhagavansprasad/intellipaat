import math

def question_01():
    n = 10; r = 5; p = 100    
    A = p * ((1 + float(r/100)) ** n)
    print(A)

def question_16():
    Country = {
        "India" : "Delhi",
        "China" : "Beijing",
        "Japan" : "Tokyo",
        "Qatar" : "Doha",
        "France" : "Marseilles",
    }
    Country["France"] = "Paris"
    Country.update("France", "Paris")

def q19_pythagorean_triplets(n):
    triplets = []
    for m in range(1, int(n**0.5) + 1):
        for n in range(1, m):
            a = m**2 - n**2
            b = 2 * m * n
            c = m**2 + n**2
            if c > n:
                break
            triplets.append((a, b, c))
    return triplets

def q19_pythagorean_triplets(n):
    triplets = []
    for i in range(1, n-1):
        for j in range(i, n):
            h = i**2 + j**2
            h = math.sqrt(h)
            
            triplets.append((i, j, h))
    return triplets

def main():

    question_01()

    # Aswers to Q2 to A18
    # Q2 - None
    # Q3 - a
    # Q4 - b
    # Q5 - c
    # Q6 - a
    # Q7 - d
    # Q8 - b
    # Q9 - a
    # Q10 - a
    # Q11 - c
    # Q12 - d
    # Q13 - None of the above - Correct answer is 'string'
    # Q14 - None of the above - Correct answer is 'string'
    # Q15 - d
    # Q17 - d
    # Q18 - 6
    
    n = 5
    triplets = q19_pythagorean_triplets(n)
    print(f"{n} pythagorean_triplets :{triplets}")

if __name__ == "__main__":
    main()
    
