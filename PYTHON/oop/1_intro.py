class com:
    def __init__(self,cpu,ram,hd):
        self.cpu=cpu
        self.ram=ram
        self.hd=hd





    def config(self):
        print("configurations are=",self.cpu,self.ram,self.hd)







obj1=com("i3","4gb","1Tb")
obj2=com("i5","8gb","1TB")

obj1.config()               #method-1
obj2.config()



com.config(obj1)        # method-2  rarely use
com.config(obj2)        # method-2  rarely use
