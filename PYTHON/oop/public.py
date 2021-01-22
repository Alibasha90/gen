class school:
    name="oxford"

    def __init__(self,roll,sec):
        self.roll=roll
        self.sec=sec
 

    def disp(self):
        print(self.roll,self.sec,school.name)




s1=school(123,"B")
s2=school(123,"B")

school.name="islam techno"
s1.disp()
s2.disp()



#here if you can access the public varibles like


#    self.name   ---> instance varible
#    school.name ----> class varible


#  self.name only modify in that object 
#   class.name is modify the all objects that u declared.....




