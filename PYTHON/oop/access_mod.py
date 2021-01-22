class A:
    def __init__(self):
        self.public=10
        self._pro=20
        self.__private=30
    
    def disp(self):
        print("class A")
        print(self.public,self._pro,self.__private)



class B(A):
    
    def display(self):
        print("class B")

        print(self.public)
        print(self._pro)
        print(self._A__private) # name mangling





obj=B()

#print(obj.public)
#print(obj._pro)
#print(obj._A__private)    # name mangling   ( obj._class__privatevarible )


obj.disp()
obj.display()
