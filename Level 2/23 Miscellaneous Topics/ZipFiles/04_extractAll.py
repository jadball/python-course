import os
import zipfile

os.chdir("out")

# tar = tarfile.open("MyFile.tar.gz")
# tar.extractall()
# tar.close()

zipfile.ZipFile("../zips/Perl.zip", "r").extractall()

print(os.listdir("."))
