import itertools

a = list(itertools.product('01234567', repeat=5))
a = [''.join(x) for x in a if x.count('6') == 1 and x[0] != '0']

b = list(itertools.product('1357', '6')) + list(itertools.product('6', '1357'))
b = [''.join(x) for x in b]
c = [x for x in a if sum([x.count(y) for y in b])==0]
print(len(c))
