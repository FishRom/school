import math

for i in range(1, 1000):
    a = math.ceil(math.log2(10+52+458))
    b = math.ceil(i*a/8)
    c = 862*b/2**10
    print(c, i)
    if c > 276:
        break