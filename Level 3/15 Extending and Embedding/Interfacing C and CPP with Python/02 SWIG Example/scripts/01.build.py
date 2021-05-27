import os
import sys

sys.path.append('../..')

os.system("swig -version")
os.chdir("../src")
os.system("python setup.py -v build_ext")
