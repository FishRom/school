import math

alfa = math.ceil(math.log2(10+2022))
b = math.ceil((alfa*158)/8)

v = (b * 15360)/1024
print(v)