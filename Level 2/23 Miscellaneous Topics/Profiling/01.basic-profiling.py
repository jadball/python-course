import cProfile
import sys

sys.path.append("src")
cProfile.run('myprogram.foo()')
