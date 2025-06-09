import math

alfa = math.ceil(math.log2(10+4000))
b = math.ceil((alfa*141)/8)
v = (2560*b)/1024
print(v)