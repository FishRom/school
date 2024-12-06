import itertools

a = list(itertools.product('0123456789AB', repeat=5))
a = [''.join(x) for x in a if x[0] != '0']

c = ['A', 'B', '9']
b = [x for x in a if x.count('7') == 1 and x.count('A') + x.count('B') + x.count('9') <= 3]

print(len(b))