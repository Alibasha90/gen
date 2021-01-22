class school:
    def __init__(self,x,y):
        self.x=x
        self.y=y



    def add(self,a,b):
        s=a+b
        return s

    def add(self,a,b,c):
        s=a+b+c
        return s






s1=school(5,5)

print(s1.add(1,2,3))
