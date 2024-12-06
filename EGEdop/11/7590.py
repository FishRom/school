import math

a = math.ceil(math.log2(2035))
b = math.ceil(a*113/8)
c = (b * 32768)/2**10

print(c)