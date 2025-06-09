import itertools

a = list(itertools.product('КОМПЬЮТЕР', repeat=5))
a = [''.join(x) for x in a]
a.sort()
b = [x for x in a if x[0] != 'Ь' and x.count('К') == 2]
print([a.index(x) + 1 for x in b[-5:]])