############################################################
#
#    multiple plots
#
############################################################

import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 5.0, 0.5)
redDashes = "r--"
blueSquares = "bs"
greenTriangles = "g^"

# create a group of axes arranged in a grid of rows and columns
row = 2
columns = 3
fig, axes = plt.subplots(row, columns, sharey=True)

axes[0][0].plot(t, t, redDashes)
axes[0][1].plot(t, t ** 2, blueSquares)
axes[0][2].plot(t, t ** 3, greenTriangles)
axes[1][0].plot(t, t + t ** 2, blueSquares)
axes[1][1].plot(t, t + t ** 3, greenTriangles)
axes[1][2].plot(t, t + t ** 4, redDashes)

axes[0][0].set_title("axis 11")
axes[0][1].set_title("axis 12")
axes[0][2].set_title("axis 13")
axes[1][0].set_title("axis 21")
axes[1][1].set_title("axis 22")
axes[1][2].set_title("axis 23")

plt.gcf().canvas.set_window_title('Figure with 2x3 set of Axes')
plt.show()
