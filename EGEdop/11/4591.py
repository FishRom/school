import math

a = math.ceil(math.log2(1710))
b = math.ceil((a*252)/8) #размер индификатора переводим в байты
c = (b * 4096)/2**10

print(c)