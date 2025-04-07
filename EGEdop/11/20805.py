import math

for x in range(1, 1000):
    alfabet = math.ceil(math.log2(x))
    a = math.ceil((alfabet*248)/8)
    v = a*75600
    if v > 16 * 2**20:
        print(v, 16 * 2**20, 75600*248)
        print(x)
        break