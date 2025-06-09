import math

for x in range(1, 50000):
    alfa = math.ceil(math.log2(x))
    bytes =math.ceil((alfa * 261)/8)
    v = bytes * 252_000
    if v > 31*2**20:
        print(x)
        break