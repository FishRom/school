import math

for i in range(1, 1000):
    a = math.ceil(math.log2(52+10+458))
    b = math.ceil((a*i)/8)
    c = (b*862)/1024
    print(c, i)
    if c > 276:
        break