import os
import sys

sys.path.append('../..')

os.chdir("../src")

installedFiles = open("files.txt", "r")
for file in installedFiles:
    file = file.rstrip()
    if file.endswith("egg-info"):
        try:
            f = open(file, 'r')
            print(f.read())
        except:
            pass
