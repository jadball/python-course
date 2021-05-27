import os
import subprocess
import sys

sys.path.append('../..')

os.chdir("../src")

try:
    installedFiles = open("files.txt", "r")
    for file in installedFiles:
        subprocess.call(f"rm {file}".split())
    subprocess.call("rm files.txt".split())
except FileNotFoundError:
    pass

print()
print("Example uninstalled")
