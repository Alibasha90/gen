class A:
    def f1(self):
        print("feature 1")

    def f2(self):
        print("feature 2")



class B:
    def f3(self):
        print("feature 3")

    def f4(self):
        print("feature 4")


class C(A,B):
    def f1(self):
        super().f1()
        print("feature 1-c")



#a1=A()   parent class----> A class only access the feature 1 , feature 2

#a1.f1()
#a1.f2()


#b1.B()   Parent class ----> B class only can access feature 3 , feature 4
#b1.f3()
#b1.f4()

c1=C() # child class --->  All features can access 

c1.f1()
#c1.f2()
#c1.f3()
#c1.f4()
#c1.f5()

