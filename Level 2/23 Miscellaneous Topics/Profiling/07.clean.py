import shutil

try:
    shutil.rmtree("html")
except:
    pass

try:
    shutil.rmtree("stats")
except:
    pass
