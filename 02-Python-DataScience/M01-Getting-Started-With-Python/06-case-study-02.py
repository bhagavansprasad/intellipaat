num_list = [2, 4, 7, 10, 11, 24, 23, 29]
num_list2 = [2, 7, 10, 23, 29]


def question_01():
    t1 = (10, 20, 30)
    t2 = (40, 50, 60)
    
    t_combine = t1 + t2
    print(f"combined tuple :{t_combine}")
    
    threetimes_t = 3 * t_combine
    print(f"threetimes_t :{threetimes_t}")
    
    print(f"third element :{threetimes_t[2]}")

    print(f"First 3 elements :{threetimes_t[:3]}")
    
    print(f"Last 3 elements :{threetimes_t[-3:]}")
    print()

    

def question_02():
    tlist = [(1, 2, 3), ("a", "b", "c"), (True, False)]
    
    print(tlist)
    print()

def question_03():
    tlist = [(1, 2, 3), ("a", "b", "c"), (True, False)]
    
    tlist.append((1, 'a', True))
    tlist.append(["sparta", "123+"])
    print(tlist)
    print()

def question_04():
    
    fruit = {"Fruit" : ('Apple', 'Banana', 'Mango','Guava'), 'Cost': (85, 54, 120, 70)}

    print(fruit['Fruit'])
    print(fruit['Cost'])
    print()

def question_04():
    tset = {1, 1, 'a', 'a', True, True}
    
    print(tset)
    print()
    
def main():
    question_01()
    question_02()
    question_03()
    question_04()
    
if __name__ == "__main__":
    main()
    