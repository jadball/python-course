from math import sin

import matplotlib.pyplot as plt
import numpy as np


def SinC(t):
    ''' sine cardinal '''
    if t == 0:
        return 1
    else:
        return sin(t) / t


SinC = np.vectorize(SinC)

t = np.arange(-50, 50, 0.01)
plt.plot(t, SinC(t))
plt.grid(True)
plt.show()
