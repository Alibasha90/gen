class car:

    color="RED"             # CLASS VARIABLE global to all objects                            # modification can be affect to other                             # objects....



    def __init__(self):
        self.mil=10           # instance varibles can't affect to 
        self.company="BMW"    # the other objects.


c1=car()
c2=car()

c1.company="AUDI"           
c1.mil=15
c1.color="PURPLE"
#car.color="purple"          # it changes to all objects...

print(c1.mil,c1.company,c1.color)
print(c2.mil,c2.company,c2.color)

