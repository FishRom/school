import math

for x in range(1, 1000):
    alfa = math.ceil(math.log2(26+26+20))
    b = math.ceil((alfa*10)/8)
    if (b + x) * 21 == 4200:
        print(x)