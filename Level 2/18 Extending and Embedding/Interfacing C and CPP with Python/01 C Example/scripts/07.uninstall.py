import os
import subprocess
import sys

sys.path.append('../..')

os.chdir("../src")

installedFiles = open("files.txt", "r")
for file in installedFiles:
    subprocess.call(f"rm {file}".split())

subprocess.call("rm files.txt".split())
print()
print("Example uninstalled")
