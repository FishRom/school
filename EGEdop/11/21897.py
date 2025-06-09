import math

for x in range(1, 1000):
    alfa = math.ceil(math.log2(x))
    b = math.ceil((alfa*246)/8)
    if (b * 703_569)/2**20 <= 77:
        print(x)