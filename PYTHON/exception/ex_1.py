

try:
#    print(10/10)
#    print("hello") #  it won't run next line , if gotten error..
    l=[10,20,30,40]
#    print(a)
#    total=reduce(lambda x,y:x+y,l)
#    print(total)
    it=iter(l)


    print(next(it))
#    print(next(it))
#    print(next(it))
#    print(next(it))
#    print(next(it))
#    print(next(it))
#    print("list is over")

except ZeroDivisionError as z:
    print(z)

except StopIteration as st:
    print(st)

except ImportError as e:
    print(e)
except NameError as e:
    print(e)

except:
    print("something went wrong")

finally:
    print("finall")

