def question_01():
    mylist = [0, 20, 30, 'apple', True, 8.10]
    print(f"mylist :{mylist}")
    
    mylist.append(30)
    mylist.append(40)
    print(f"mylist :{mylist}")
    
    try:
        reversedList = mylist.sort(reverse=True)
        print(f"reversedList :{reversedList}")
    except Exception as err:
        print(f"Sorting is not allowed :{err}")

def question_02():
    ddata = {'data': 1, 'infomation': 2, 'text': 3}
    
    ddata.pop('text')
    ddata['features'] = 4
    print(ddata['data'])
    
    print(ddata)

def question_03():
    my_tuple = (1, 2, 3, 'apple', 'mango')
    print(f"my_tuple :{my_tuple}")

def question_04():
    numeric_tuple = (10, 20, 30, 40, 50)
    my_tuple = (1, 2, 3, 'apple', 'mango')
    
    print(f"numeric_tuple :{numeric_tuple}")
    print(f"min value     :{min(numeric_tuple)}")
    
    r1 = my_tuple + numeric_tuple
    print(f"r1 :{r1}")
    
    newdupli = my_tuple * 2
    print(f"newdupli :{newdupli}")

def question_05():
    set1 = {1,2,3,4,5} 
    set2 = {2,3,7,6,1}
    
    print(f"set1 :{set1}")
    print(f"set2 :{set2}")
    print(f"Union of s1 and s2        :{set1|set2}")
    print(f"Intersection of s1 and s2 :{set1 & set2}")
    print(f"difference   of s1 and s2 :{set1.difference(set2)}")
    
def main():
    question_01()
    question_02()
    question_03()
    question_04()
    question_05()
    
if __name__ == "__main__":
    main()
    
    