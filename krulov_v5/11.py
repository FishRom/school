import math

alfa = math.ceil(math.log2(10+60))
bytes = math.ceil((alfa*108)/8)
v = ((bytes*25600)/1024)
print(v)