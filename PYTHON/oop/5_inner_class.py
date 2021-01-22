class A:
    def __init__(self,name,age):
        self.name =name
        self.age= age
        self.var=self.B()

    def show(self):
        print("user name={}\nage={}".format(self.name,self.age) )
        self.var.show()


    class B:
        def __init__(self):
            self.place="parchoor"
            self.pin=12345

        def show(self):
            print("my place={}\nmy pincode={}".format(self.place,self.pin) )


#data=input("enter the name=")
#age=int(input("enter the age="))
#obj1=A(data,age);



obj1=A("Ali",25)

obj1.show()     # calling the method





