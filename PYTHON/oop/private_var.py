class Geek: 

    # private members 
    __var1 = 10
    __roll = None
    __branch = None

     # constructor 
    def __init__(self, name, roll, branch):   
        self.__name = name 
        self.__roll = roll 
        self.__branch = branch

     # private member function   
    def __displayDetails(self): 

        # accessing private data members 
        print("Name: ", self.__name) 
        print("Roll: ", self.__roll) 
        print("Branch: ", self.__branch) 
        print("var in global: ", self.__var1) 

     # public member function 
    def accessPrivateFunction(self):  

        # accesing private member function 
        self.__displayDetails()


#    @classmethod
    def method_of_class(self):
        print(self.__var1)





# creating object     
obj = Geek("R2J", 1706256, "Information Technology") 

# calling public member function of the class 
obj.accessPrivateFunction()
obj.method_of_class()
