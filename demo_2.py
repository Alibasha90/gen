import demo
from ctypes import *


so_file="./my_cfile.so"

my_var=CDLL(so_file)

my_var.main()

