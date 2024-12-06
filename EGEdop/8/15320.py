import itertools

a = list(itertools.product('ПАРУС', repeat=5))
a = [''.join(x) for x in a]

a.sort()
b = [x for x in a if x.count('У') <= 1 and x.count('АА') == 0][0]
print(a.index(b) + 1)