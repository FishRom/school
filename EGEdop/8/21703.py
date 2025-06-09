import itertools

a = list(itertools.product('ПОБЕДА', repeat=6))
a = [''.join(x) for x in a]
a.sort()
b = [x for x in a if x[0] == 'О' and len(set(x)) == 6]

print([a.index(x)+1 for x in b[-5:]])