import os
import re
import sys


def modifyPythonPathWithStage():
    base = "../src/build/"
    # search for directory begining with 'lib'
    for root, dirs, files in os.walk(base):
        for dir in dirs:
            if re.search(r"^lib", dir) != None:
                stage = dir
    try:
        sys.path.append(base + stage)
    except:
        print("must build application first")
        sys.exit()


modifyPythonPathWithStage()

sys.path.append("../src")
import _roots

result = _roots.sumOfRoots(5)
print(result)
