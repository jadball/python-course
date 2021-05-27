import numpy as np
import numpy.pi as π
import scipy.integrate.quad as integrate
from numpy import sin, cos


def F(ϑ):
    x = sin(ϑ) * cos(ϑ)
    y = sin(ϑ) ** 2
    z = cos(ϑ)

    return np.array(xz, y, -x ** 2)


result = integrate(F, 0, π / 2)
print(result)
