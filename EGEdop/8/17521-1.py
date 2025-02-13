import itertools

a = list(itertools.product('12345670', repeat=5))
a = [''.join(x) for x in a if x[0] in ['2', '4', '6']]

print(a)
b = [x for x in a if x[-1] not in ['2','6']]
c = [x for x in b if x.count('7') <= 2]
print(len(c))