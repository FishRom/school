import itertools

a = list(itertools.permutations('1234567890ABCDEF', r=4))
a = [''.join(x) for x in a if x[0] != '0']
b = list(itertools.product('13579BDF', repeat=2)) + list(itertools.product('24680ACE', repeat=2))
b = [''.join(x) for x in b]
c = [x for x in a if sum([x.count(y) for y in b]) == 0]
print(len(c))