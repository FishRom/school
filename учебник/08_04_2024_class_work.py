'''import math

def perebor(x):
    return x - math.cos(x)

eps = 0.001
x = 0
delta = 2 * eps
while perebor(x) * perebor(x + delta) > 0:
    x = x + delta
print(f'x = {x + eps:.3f}')'''

'''import math
def f(x):
    f = x - math.cos(x)
    return f


eps = 0.001
a = int(input())
b = int(input())
delta = 2 * eps
while b - a > delta:
    c = (a + b) / 2
    if f(a) * f(c) <= 0:
        b = c
    else:
        a = c
print('x = ', (a + b))'''

import math
def f(x):
    f = 10 * math.tan(x) - 9.8 * 10 ** 2 // 2 * 12 ** 2 * math.cos(x) ** 2 - 4
    return f


pi = 3.1415926
eps = 0.001
u = 0
delta = 2 * eps
while u < pi / 2:
    if f(u) * f(u + delta) <= 0:
        print('Угол', (u + eps) * 180 / pi, 'градусов')
    u += delta
