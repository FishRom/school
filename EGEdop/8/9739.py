import itertools

a = list(itertools.product('МАНГУСТ', repeat=6))
a = [''.join(x) for x in a]

a.sort()
b = [x for x in a if x[0] != 'У' and x.count('М') == 2 and x.count('Г') <= 1][-1]
print(a.index(b) + 1)