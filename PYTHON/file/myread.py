fd=open("readfile","r")

#fd.write("hello ali u created file\n")

#data=fd.read(10) # 10 bytes only can read

fd.fseek(0,2) # one line can read at once .....
pos=fd.tell()

fd.fseek(0,0) # one line can read at once .....

pos=fd.tell()


print(pos)



#fd.seek(0,0) # one line can read at once .....

data=fd.read(5)

print(data)

fd.close()
