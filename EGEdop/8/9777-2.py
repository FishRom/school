import itertools

a = list(itertools.product('КОМПЬЮТЕР', repeat=5))
a = [''.join(x) for x in a]
a.sort()

b = [x for x in a if x.count('К') == 2 and x[0] != 'Ь']
b.sort()
print([a.index(x) + 1 for x in b[-10:]])