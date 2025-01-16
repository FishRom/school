import itertools

a = list(itertools.permutations('1234567890ABCDEF', r=3))
a = [''.join(x) for x in a if x[0] != '0']
b = list(itertools.product('24680ACE', '24680ACE')) +list(itertools.product( '13579BDF', '13579BDF'))
b = [''.join(x) for x in b]
#z = '123'
#print([z.count(y) for y in b])
c = [x for x in a if sum([x.count(y) for y in b]) == 0]
print(len(c))

#b = [x for x in a if ]

