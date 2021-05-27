import os
import py_compile

py_compile.compile("myfile.py")
os.system("ls -lR myfile.* __pycache__")
