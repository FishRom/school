import math

for x in range(1, 1000):
    alfa = math.ceil(math.log2(x))
    bytes = math.ceil((alfa*257)/8)
    if (bytes*295_740)/2**20 <= 33:
        print(x)
    else:
        break