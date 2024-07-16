def sortitem(item):
    return item[1]

def max_score(td):
    tlist = []
    for match in td:
        for item in td[match].items():
            tlist.append(item)


    tlist = sorted(tlist, key=sortitem)
    
    return tlist[-1]

def main():
    d1 = {'test1':{'Dhoni':56, 'Balaji' : 85}, 'test2':{'Dhoni': 87, 'Balaji': 200}}
    d2 = {'test1':{'Dhoni':56, 'Balaji' : 85}, 'test2':{'Dhoni': 300, 'Balaji': 87}}
    d3 = {'test1':{'Dhoni':56, 'Balaji' : 400}, 'test2':{'Dhoni': 87, 'Balaji': 200}}
    d4 = {'test1':{'Dhoni':500, 'Balaji' : 85}, 'test2':{'Dhoni': 87, 'Balaji': 200}}
    
    print(max_score(d1))
    print(max_score(d2))
    print(max_score(d3))
    print(max_score(d4))

if __name__ == "__main__":
    main()
