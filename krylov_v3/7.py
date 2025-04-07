import math

i = math.ceil(math.log2(2048))
v = 128*2048*i
n = (81_920*600)/v
print(n)

