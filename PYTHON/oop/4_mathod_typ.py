class school:
    
    school="oxford"
    
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    
    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    def grade(self):

        total = (self.m1+self.m2+self.m3) / 3
        
        if(total > 80):
            print("pass {}".format(self)  )
        else:
            print("failed={}".format(self) )

    @classmethod
    def getinfo(cls,var):
        cls.var=var
        print(cls.var)
        return (cls.school)

    @staticmethod
    def info():
        print("this static method....")

st1=school(80,80,90)
st2=school(50,60,78)

print("student-1==",st1.avg())
print("student-2==",st2.avg())

#st1.grade()
#st2.grade()

print("students from ==", school.getinfo(1) )
print( school.info() )


