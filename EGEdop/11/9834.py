import math

alfabet = math.ceil(math.log2(52))
bytes = math.ceil((10 * alfabet)/8)
v = (bytes*65536)/1024
print(v)