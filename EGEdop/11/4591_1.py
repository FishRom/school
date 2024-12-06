import math

a = math.ceil(math.log2(10+1700)) #бит на один символ
b = math.ceil(252*a/8) #длина индификатора в байтах
c = (4096*b)/2**10 #объем
print(c)