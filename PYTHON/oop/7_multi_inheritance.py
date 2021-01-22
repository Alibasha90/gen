class A:
    def f1(self):
        print("feature 1")

    def f2(self):
        print("feature 2")



class B(A):
    def f3(self):
        print("feature 3")

    def f4(self):
        print("feature 4")


class C(B):
    def f5(self):
        print("feature 5")


obj=C()

obj.f1()
obj.f2()
obj.f3()
obj.f4()
obj.f5()


