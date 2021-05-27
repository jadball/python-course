import os
import subprocess
import sys

sys.path.append('../..')

os.chdir("../src")
subprocess.call("python setup.py -v build_ext".split())
