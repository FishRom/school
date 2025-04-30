import math

alfa = math.ceil(math.log2(1000+10))
byte = math.ceil((alfa*190)/8)
v = byte * 39424
print(v/1024)