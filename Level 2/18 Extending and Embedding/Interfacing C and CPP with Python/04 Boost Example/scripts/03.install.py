import os
import sys

sys.path.append('../..')

os.chdir("../src")

# must run build first
os.system("python setup.py install")
