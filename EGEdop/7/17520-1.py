import math

i = math.ceil(math.log2(8192))
print(i)
v1 = 1024*960*i
vo = 1474560*280
n = int(vo/v1)
print(n)