class A: 
    def rk(self): 
       # super().rk()
        print("In class A") 
class B: 
    def rk(self): 
       # super().rk()
        print("In class B") 
class C(B,A): 
#    def rk(self):
#        super().rk()
#        print("In class C") 
    pass 

#class D(B,A): 
#    def rk(self): 
#        super().rk()
#        print("In class D") 
#    pass


#class E(D,C): 
#    def rk(self):    this is my new class ,, i declared 
#        super().rk()
#        print("In class E") 

#    pass


r=C()

r.rk()
print(C.__mro__) 
print(C.mro()) 

