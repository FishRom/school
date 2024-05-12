from math import cos
def f2(x):
    return x ** 2


def f1(x):
    return 4 * cos(x)


a = -2
b = 2
h = 0.01
S = 0
x = a
while x < b:
    S += f1(x) - f2(x) + f1(x + h) - f2(x + h)
    x += h
S = h * S / 2
print(S)