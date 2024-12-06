import itertools

a = list(itertools.product('12345670', repeat=5))
a = [''.join(x) for x in a if x[0] != '0']

b = ['1', '3', '5', '7']

c = [x for x in a if x[0] not in b and x[-1] not in ['2', '6'] and x.count('7') <= 2]
print(len(c))