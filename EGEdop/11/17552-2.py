import math

for x in range(1, 1000):
    alfabet = math.ceil(math.log2(x))
    a = math.ceil((261*alfabet)/8)
    v = a*252_500
    if v > 31*2**20:
        print(x)
        break