from math import sin
import scipy.optimize


def func(y):
        x = 4*sin(y) - 4
        return x


x = scipy.optimize.fsolve(func, 0.3)
print(x)
print("hello, world!")
