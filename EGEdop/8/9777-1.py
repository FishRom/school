import itertools

a = list(itertools.product('КОМПЬЮТЕР', repeat=5))
a = [''.join(x) for x in a]
a.sort()
b = [x for x in a if x.count('К') == 2 and x[0] != 'Ь'][-5:]
print([(a.index(x)+1, x) for x in b])
print(b)