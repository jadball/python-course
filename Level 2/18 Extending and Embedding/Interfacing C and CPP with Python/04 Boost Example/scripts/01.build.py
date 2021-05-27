import os
import subprocess
import sys

sys.path.append('../..')

os.environ["ARCHFLAGS"] = "-arch x86_64"

os.system("swig -version")
os.chdir("../src")
subprocess.call('python setup.py -v build_ext'.split())
