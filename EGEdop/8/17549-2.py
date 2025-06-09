import itertools

a = list(itertools.product('ФОКУС', repeat=5))
a = [''.join(x) for x in a]
a.sort()
b = [x for x in a if x.count('Ф') == 0 and x.count('У') == 2]
print([a.index(x) + 1 for x in b[-5:]])