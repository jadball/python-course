import matplotlib.pyplot as plt

import skimage.io as io

fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(10, 4), dpi=72 * 3)
image = io.imread("images/chris.jpg", as_gray=True) * 256
t1 = 90
t2 = 116
t3 = 154

image[image < t1] = 0
image[(image > t1) & (image <= t2)] = t2
image[(image > t2) & (image <= t3)] = t3
image[image > t3] = 255

plt.axis('off')
ax.imshow(image, cmap=plt.cm.gray)
plt.savefig("out/chris_in_gray.pdf")
plt.show()
