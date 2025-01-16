import math

alfabet = math.ceil(math.log2(4080+10))
byte_one_ind = math.ceil((79*alfabet/8))
v = (byte_one_ind * 65536)/2**10
print(v)