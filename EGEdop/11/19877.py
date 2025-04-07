import math

alfabet_1 = math.ceil(math.log2(26))
bites_1 = math.ceil(4*alfabet_1)

alfa = math.ceil(math.log2(1025))
bites_2 = math.ceil(70*alfa)

v1 = (24*1024*1024*8)/131_072

v_dop = v1 - bites_1 - bites_2
print(v_dop/8)