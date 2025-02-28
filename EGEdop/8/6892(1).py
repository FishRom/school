import itertools

a = list(itertools.product('012345', repeat=6))
a = [''.join(x) for x in a if  x[0] != '0']

b = list(itertools.product('135', '2')) + list(itertools.product('2', '135'))
b = [''.join(x) for x in b]

c = [x for x in a if x.count('2') == 1 and sum([x.count(y) for y in b]) == 0]
print(len(c))