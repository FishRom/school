import itertools

a = list(itertools.product('ПОБЕДА', repeat=6))

b = [x for x in a if len(x) == len(set(x)) and x[0] == 'О']
a.sort()
b.sort()

a = [''.join(x) for x in a]
b = [''.join(x) for x in b]

print([(a.index(x) + 1, x) for x in b[-5:]])