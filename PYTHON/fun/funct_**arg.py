def fun(*Args):
    print(type(Args))
    for i in Args:
        print(i)


def fun2(**Args):
    print(type(Args))
    for i,j in Args.items():
        print("{}={}".format(i,j))


def pass_dict(d):
    print("This is pass_dict method =",type(d))
    for i ,j in d.items():
        print(i,j)

fun(1,2,3,45,5)
fun2(first='ali',seecond='ashu')
d={"1234":"ali",2:"ashu"}
print(pass_dict(d))
