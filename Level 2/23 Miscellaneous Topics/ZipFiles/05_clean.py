import os
import shutil

outDirectory = "out"
shutil.rmtree(outDirectory)
os.mkdir("out")

outDirectory = "files/Compressed"
shutil.rmtree(outDirectory)
