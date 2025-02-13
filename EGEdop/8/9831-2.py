import itertools

a = list(itertools.permutations('1234567890ABCDEF', r=3))
d = list(itertools.product('13579BDF', repeat=2)) + list(itertools.product('24680ACE', repeat=2))
d = [''.join(x) for x in d]
print(d)
a = [''.join(x) for x in a if x[0] != '0']

b = [x for x in a if sum([x.count(y) for y in d]) == 0]
print(len(b))