import subprocess 
import os


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

if(os.path.isfile("./target")):
    subprocess.run( ["make","rm"] )
else:
    subprocess.run( ["make"] )
#subprocess.run( ["make","run"] ,input="1\n5\n66\n45\n33\n21\n34".encode())
#subprocess.run( ["make","rm"] )


