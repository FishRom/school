import math

alfabet = math.ceil(math.log2(1500+10))
a = math.ceil((105*alfabet)/8)
v = (16_384*a)/1024
print(v)
