############################################################
#
#    ordinary differential equations
#
############################################################

from math import *

from scipy.integrate import odeint

# evaluate dy/dt = y
# for initial value of y = y0
# and a time range from t0 ... t1
y0 = 7
t0 = 2
t1 = 6
# solution: y  = e**(t  + k)
# where     y0 = e**(t0 + k)
#  =>       k  = log(y0) - t0
print("calculated result")
print(odeint(lambda y, t: y, y0, [t0, t1]))

print("analytical result")
k = log(y0) - t0;
print([y0, e ** (t1 + k)])

1
