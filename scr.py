import subprocess 
#import test_c.c


"""subprocess.run("ls")
subprocess.run(["python3", "demo.py"])
subprocess.run("./a.out")"""


"""result=subprocess.run("ls",stdout=subprocess.PIPE)
result.stdout"""


#subprocess.run(["python3","demo.py"],input="Ali\nashu",universal_newlines=True)
#subprocess.run(["python3","demo.py"],input="Ali\nashu".encode())

#subprocess.run(["python3","demo.py"],input="Ali\nashu".encode())
#subprocess.run(["sleep","3"])
#subprocess.run(["python3","demo.py"],input="Ali\nashu".encode())

#subprocess.run( ["cd mysort/make"] )
#subprocess.run( ["cd mysort/make run"] )
subprocess.run( ["python3", "demo.py"] )



