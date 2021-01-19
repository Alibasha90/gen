fd=open("text","r+")

fd.write("hello")

#fd.close()

#fd=open("text","r")

out=fd.read(10)
print("output is:",out)
print("file name:=",fd.name)
print("file name:=",fd.mode)
print("file name:=",fd.closed)

fd.close()
