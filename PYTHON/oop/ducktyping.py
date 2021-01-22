class pycharm:
    def fun(self):
        print("my pycharm")


class editor:
    def fun(self):
        print("my new edition ")
        print("my pycharm")




class lapy:
    def code(self,ide):
        ide.fun()




A1=pycharm()    # here we achieve the poly-morphism by using the duck typing..  
A2=editor()


obj_2=lapy()
obj_2.code(A1)
obj_2.code(A2)
