import numpy as np
from numpy import cos, sin, arctan


def rotate(vector, θ, 𝜙):
    matrix = [
        [sin(θ) * cos(𝜙), cos(θ) * cos(𝜙), -sin(𝜙)],
        [sin(θ) * sin(𝜙), cos(θ) * sin(𝜙), cos(𝜙)],
        [cos(θ), -sin(θ), 0]
    ]
    m = np.array(matrix)  # convert to Numpy array
    return m @ vector  # note: @ denotes matrix multiplication


π = 4 * arctan(1.0)
print(rotate(np.array([10, 10, 10]), π / 3, π / 4))
