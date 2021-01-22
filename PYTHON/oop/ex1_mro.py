class A:
    def __init__(self,name, age ):
        self.name=name
        self.age=age

    def display(self):
        printf("name ={}\nage={}".format(self.name,self.age))


class B(A):
    def display(self):
        super().display()


obj=B("ali",25)

print(help(B))


