import itertools

a = list(itertools.product('АВЛОР', repeat=4))
a = [''.join(x) for x in a]

a.sort()
b = [x for x in a if x[0] == 'Л'][0]
print(a.index(b) + 1)
print(b[:20])