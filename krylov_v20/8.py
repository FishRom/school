import itertools

a = list(itertools.product('01234', repeat=3))
a = [''.join(x) for x in a if x[0] != '0']
print(a)
b = [x for x in a if (int(x) // 100) > (int(x) // 10) > (int(x) % 10)]
print(b)
'''print(123//100) #1 разряд
print((123 // 10) % 10) # 2 разряд
print(123%10) # 3 разряд'''