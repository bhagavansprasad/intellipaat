class base:
    apub = 10
    _bprot = 20
    __cpriv = 30
    
    def __init__(self, a, b, c):
        self.apub = a
        self._bprot = b
        self.__cpriv = c
        
    def base_display(self):
        print(f"Base: apub    :{self.apub}")
        print(f"Base: _bprot  :{self._bprot}")
        print(f"Base: __cpriv :{self.__cpriv}")
        print()

class derived(base):
    def derived_display(self):
        print(f"derived: apub    :{self.apub}")
        print(f"derived: _bprot  :{self._bprot}")
        # print(f"derived: __cpriv :{self.__cpriv}")
        print()

def main():
    derived_obj = derived(10, 20, 30)
    derived_obj.base_display()
    derived_obj.derived_display()
    
    print(f"DObj : apub    :{derived_obj.apub}")
    print(f"DObj : _bprot  :{derived_obj._bprot}")
    # print(f"DObj : __cpriv :{derived_obj.__cpriv}")
    print()

    base_obj = base(50, 60, 70)
    print(f"base_obj : apub    :{base_obj.apub}")
    print(f"base_obj : _bprot  :{base_obj._bprot}")
    print(f"base_obj : __cpriv :{base_obj.__cpriv}")
    
if __name__ == "__main__":
    main()
    


