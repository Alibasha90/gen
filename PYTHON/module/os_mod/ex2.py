import os



#print(os.stat("ex1.py"))
#print(os.stat("ex1.py").st_size,"bytes")

var=os.walk("/home/ali/Downloads")

for path,dirname,filename in var:
    print("path=",path)
    print("dirname=",dirname)
    print("filename=",filename)

