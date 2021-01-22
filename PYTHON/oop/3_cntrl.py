#note:-

# self is a parameter , we can access the attributes and methods 
# in class , we can change the name instead self.
# and refering the objects as well.

# constructor is usually initiating an objects.
# The task of the constructor is to initialize the data members of# the class when object is created.

class computer:
    def __init__(myself):
        myself.name="Ali"
        myself.age=25

    def update(myself):
        myself.name="mohammadh"
        myself.age=40


    def compare(myself,other):
        if(myself.age==other.age):
            return 1
        else:
            return 0


c1=computer()
c2=computer()

c1.update()

if c1.compare(c2):
    print("they are same age")

else:
    print("not same their ages")
#c1.name="Ashnadh"
#c1.age=30


print(c1.name)
print(c1.age)
print(c2.name)
print(c2.age)

#print("id of c1={}\nc2 id ={}".format( id(c1),id(c2)) )



