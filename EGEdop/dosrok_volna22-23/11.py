import math

alfabet = math.ceil(math.log2(10 + 2025))
bytes_one = math.ceil((113*alfabet)/8)
v = ((bytes_one*32768)/1024)

print(v)