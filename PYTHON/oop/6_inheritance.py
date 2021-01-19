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




obj=B()

obj.f1()
