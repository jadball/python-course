import os
import sys

bin = os.path.dirname(sys.executable) + os.pathsep
os.environ["PATH"] = bin + os.environ["PATH"]
# print(os.environ["PATH"])
