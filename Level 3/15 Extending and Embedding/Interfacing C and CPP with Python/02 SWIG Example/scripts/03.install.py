import os
import subprocess
import sys

sys.path.append('../..')

os.chdir("../src")

# must run build first
subprocess.call("python setup.py install --record files.txt --user".split())
print("\n\nThe following files were installed:")
subprocess.call("cat files.txt".split())
