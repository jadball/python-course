from math import pi as π
from math import sin

import matplotlib.pyplot as plt
import numpy as np


def sinusoidal(t, A, ω, ϕ):
    ''' x(t)=Asin(ωt+ϕ) '''
    return A * sin(ω * t + ϕ)


sinusoidal = np.vectorize(sinusoidal)

t = np.arange(-10, 10, 0.01)
plt.plot(t, sinusoidal(t, A=3, ω=π / 4, ϕ=π / 3))
plt.grid(True)
plt.show()
