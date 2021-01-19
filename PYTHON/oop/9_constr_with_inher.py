class A:
    def __init__(self):
        print("this is A init")


    def f1(self):
        print("feature 1-A")


    def f2(self):
        print("feature 2-A")


class B(A):
    def __init__(self):
        super().__init__()
        print("this is B init")


    def f1(self):
        super().f1()
        print("feature 1-B")

    def f2(self):
        super().f2()
        print("feature 2-B")




obj=B()

obj.f1()
obj.f2()





