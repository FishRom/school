import math
for x in range(1, 1000):
    alfabet = math.ceil(math.log2(62 + 458))
    a = math.ceil((x*alfabet)/8)
    v = 862*a
    if v > 276*2**10:
        break
    else:
        print(x)