try:
 #   print(a)
    fd=open("f1","r+")
    fd.write("hello")

except NameError as e:   # name error here  a not defined
    print(e)

except FileNotFoundError as e:  # file not found error 
    print(e)


except IndentationError as e:
    print(e)
    
