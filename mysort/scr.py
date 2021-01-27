import subprocess 
import os

n=5

if(os.path.isfile("./target")):
    subprocess.run( ["make","rm"] )
else:
    subprocess.run( ["make"] )
    for i in range(1,6):
        print("i=",i)
        for a in range(5,10):
            print("a=",a)
            for b in range(10,5,-1):
                print("b=",b)
                for c in range(10,15,-1):

                    print("c=",c)
                    for d in range(15,20):

                        print("d=",d)
                        for e in range(20,15,-1):
                            print(a,b,c,d,e)
                            subprocess.run( ["make","run"] ,input="i\n  n\n  a\nb\nc\nd\ne".encode())
                            print("i m done")


