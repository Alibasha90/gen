class A:
    def __init__(self):
        print("class A init")

    def f1(self):
<<<<<<< HEAD
        print("feature 1")

    def f2(self):
        print("feature 2")



class B(A):
    def __init__(self):
        print("class B init")

    def f3(self):
        print("feature 3")

    def f4(self):
        print("feature 4")


class C(A):
    def __init__(self):
        print("class C init")

    def f5(self):
        print("feature 5")

    def f6(self):
        print("feature 6")


class D(B,C):
    def __init__(self):
        print("class D init")

    def f7(self):
        print("feature 7")


    def f8(self):
        print("feature 8")



obj=D()

#obj.f1()
#obj.f2()
#obj.f3()
#obj.f4()
=======
        print("feature 1-A")
        super().f1()

    def f2(self):
        print("feature 2-B")



class B:
    def __init__(self):
        print("class B init")

    def f1(self):
        #super().f1()
        print("feature 1-B")
        super().f1()

    def f2(self):
        print("feature 2-B")


class C(B,A):
    def __init__(self):
        print("class C init")

    def f1(self):
        print("feature 1-C")
        super().f1()

    def f2(self):
        print("feature 2-C")


class D(A,B):
    def __init__(self):
        print("class D init")

    def f1(self):
        print("feature 1-D")
        super().f1()


    def f2(self):
        print("feature 2-D")


class E(D,C):


    def __init__(self):
        print("class E init")

    def f1(self):
        #super().f1()
        print("feature 1-E")
        super().f1()

    def f2(self):
        print("feature 2-E")


obj=E()
#print(help(E))

obj.f1()
#obj.f2()
#obj.f3()
#obj.f4(
>>>>>>> 8932b92172a779b08612b77aab6eb3c6865959a7
#obj.f5()
#obj.f6()
#obj.f7()
#obj.f8()

