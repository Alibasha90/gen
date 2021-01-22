# method -1

def fun1(sh):

    print("fun is called ")
    return sh

def show():
    return "this is show "




try:

    v=fun1(show)

    print(v() )




except NameError as err:
    print(err)
