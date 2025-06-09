import itertools

a = list(itertools.product('МАНГУСТ', repeat=6))
a = [''.join(x) for x in a]
a.sort()

c = [x for x in a if x[0] != 'У' and x.count('М') == 2 and x.count('Г') <= 1]
print([a.index(x) + 1 for x in c[-5:]])
print(a.index(c[-1]) + 1)