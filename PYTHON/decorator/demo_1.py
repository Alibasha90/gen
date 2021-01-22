def modify(fun):
    def inner():
   #     x=eval(input("enter the int="))
  #      y=eval(input("enter the int="))
        fun()
        if(type(x)==type(1) and type(y) == type(1) ):
            print("both are int.. here we go result....!")
            sum=x+y
            print("total=",sum)

        else:
            print("plzzz enter integer values")

        return inner





@modify
def add():
    x=eval(input("enter the int="))
    y=eval(input("enter the int="))

    #sum=x+y
   # print("total is =",sum)



tot_retun=modify(add)
print("hello")
tot_retun()

