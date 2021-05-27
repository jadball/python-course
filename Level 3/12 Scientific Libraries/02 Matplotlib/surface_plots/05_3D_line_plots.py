import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')
t = np.arange(0, 10, 0.01)
z = t
x = 2 * t ** 3 + 1
y = 2 * t ** 2

# x, y and z are 1D arrays
ax.plot(x, y, z, label='parametric curve')
ax.legend()

plt.show()
