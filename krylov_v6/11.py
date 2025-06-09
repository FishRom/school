import math

alfa = math.ceil(math.log2(910))
bytes = math.ceil((alfa*331)/8)
v = (bytes*1536)/2**10
print(v)