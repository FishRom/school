import math

p = math.ceil(math.log2(8192))
v1 = 1024*960*p
r = 0
for i in range(5000):
    if 1_474_560 * 280 >= v1*i:
        print(i)
    else:
        break

print(1_474_560 * 280/(1024*960*p))

