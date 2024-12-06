import math

a = math.ceil(math.log2(10+4550))
b = math.ceil(294*a/8) #здесь уже байты!!!
c = 131072*b/2**10
print(c)