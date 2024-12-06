import itertools

a = list(itertools.product('ABCD123456789', repeat=5))
a = [''.join(x) for x in a]

a.sort()
b = [x for x in a if x.count('8') == 1 and x.count('A')][0]
print(len(b))
