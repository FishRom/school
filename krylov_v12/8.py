import itertools

a = list(itertools.product('ПОЛЬЗА', repeat=6))
a = [''.join(x) for x in a]
a.sort()
b = [x for x in a if x.count('Ь') <= 1 and x.count('А') == 1 and x.count('З') <= 2]
print([a.index(x) + 1 for x in b[:5]])