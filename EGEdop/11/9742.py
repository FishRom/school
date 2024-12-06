import math

a = math.ceil(math.log2(10+1500))
b = math.ceil(105*a/8)
c = 16384*b/2**10
print(c)