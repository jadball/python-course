############################################################
#
#    search directory tree
#
############################################################

import distutils.sysconfig
import os
import re

sitePackages = distutils.sysconfig.get_python_lib()

# search for all files with .py extension
for root, dirs, files in os.walk(sitePackages):
    for name in files:
        # note use of os.sep
        if re.search("[.]py$", name) != None:
            print(root + os.sep + name)
1
