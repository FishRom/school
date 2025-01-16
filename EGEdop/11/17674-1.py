import math

for i in range(500):
    alfabet = math.ceil(math.log2(26+10+450))
    bytes = (i*alfabet)/8
    v = (bytes*575)/1024
    print(v, i)
    if v > 100:
        break