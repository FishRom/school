import itertools

a = list(itertools.product('АВЛОР', repeat=4))
a.sort()
print(a)
a = [''.join(x) for x in a]
b = [x for x in a if x[0] == 'Л']
print(a.index('ЛААА')+1)