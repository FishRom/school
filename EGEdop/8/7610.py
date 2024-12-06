import itertools

a = list(itertools.product('АКЛМНЯ', repeat=5))
a = [''.join(x) for x in a]

a.sort()
b = [x for x in a if x[0] == 'К' and x[1] == 'М'][0]
print(a.index(b) + 1)

b = [x for x in a if str(x[:2]) == 'КМ'][0]
print(a.index(b) + 1)