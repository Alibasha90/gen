class school:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self,other):
        m1=self.m1+other.m2
        m2=self.m1+other.m2
        s3=school(m1,m2)

        return s3


    

    def __mul__(self,other):
        m1=self.m1*other.m2
        m2=self.m1*other.m2

        s3=school(m1,m2)
        return s3


    def __gt__(self,other):
        s1=self.m1+self.m2
        s2=other.m1+other.m2
        print("s1:",s1)
        print("s2:",s2)
        if s1 > s2:
            return True
        else:
            return False


        
    

stu1=school(60,50)
stu2=school(70,76)

add=stu1+stu2
mul=stu1*stu2

if stu1 > stu2:
    print("student_1 is won")

else:
    print("student_2 is won")


print(add.m1)
print(mul.m1)






