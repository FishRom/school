import itertools

a = list(itertools.product('1234567890ABC', repeat=7))
a = [''.join(x) for x in a if x[0] != 0]

b = list(itertools.product('24680AC', '24680AC')) + list(itertools.product('13579B', '13579B'))
b = [''.join(x) for x in b]
print(b)
#print(a[:40])
#a = a[:40] + ['1252521']


c = [x for x in a if sum([x.count(y) for y in b]) == 0 and x.count('5') >= 2]

print(len(c))