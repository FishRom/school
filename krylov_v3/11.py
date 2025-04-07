import math

for x in range(1, 300):
    alfa = math.ceil(math.log2(10 + 500))
    bytes = math.ceil((x*alfa)/8)
    if (bytes*1600) <= (244*1024):
        print(x)