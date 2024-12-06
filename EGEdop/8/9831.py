import itertools

a = list(itertools.permutations('ABCDEF9876543210', 3))
a = [''.join(x) for x in a if x[0] != '0']

b = list(itertools.product('ACE86420', repeat=2)) + list(itertools.product('BDF97531', repeat=2))
b = [''.join(x) for x in b]
a = [x for x in a if sum([x.count(y) for y in b]) == 0]
print(len(a))