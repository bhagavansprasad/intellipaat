class data:
    pubdata = 10
    _protdata = 20
    __privdata = 30
    
    def display(self):
        print(f"pubdata     :{self.pubdata}")
        print(f"_protdata   :{self._protdata}")
        print(f"__privdata  :{self.__privdata}") # allowed
        print()

def main():
    d = data()

    d.display()

    print(f"pubdata     :{d.pubdata}")
    print(f"_protdata   :{d._protdata}")
    try:
        print(f"__privdata  :{d.__privdata}") # not allowed
    except Exception as err:
        print(f"Access Private members is allowed ONLY from WITHIN CLASS :{err}")
        
    
    
    
if __name__ == "__main__":
    main()
