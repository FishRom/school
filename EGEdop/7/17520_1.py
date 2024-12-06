import math

v = 1024*960*math.ceil(math.log2(8192)) #ceil округляет в большую сторону
a = (1474560 * 280) / v
print(a)