class A:
    def __init__(self):
        print("this is A init")


    def f1(self):
        print("feature 1-A")


    def f2(self):
        print("feature 2-A")


class B:
    def __init__(self):
        print("this is B init")


    def f1(self):
        print("feature 1-B")

    def f2(self):
        print("feature 2-B")


<<<<<<< HEAD
class C( A , B):
=======
class C( B , A):
>>>>>>> 8932b92172a779b08612b77aab6eb3c6865959a7
#    def __init__(self):
#        super().__init__()
    
    def f1(self):
        super().f1()
        print("feature 1-C")


    def f2(self):
        super().f2()
        print("feature 2-C")


obj=C()    # init of A firstly and B...... 

<<<<<<< HEAD
obj.f1()  # based on MRO A class call first and B class....
obj.f2()




=======
#obj.f1()  # based on MRO A class call first and B class....
#obj.f2()
print(help(C))
>>>>>>> 8932b92172a779b08612b77aab6eb3c6865959a7

