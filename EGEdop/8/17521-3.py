import itertools

a = list(itertools.product('01234567', repeat=5))
a = [''.join(x) for x in a if x[0] != '0']
b = [x for x in a if x[0] in ['2', '4', '6'] and x[-1] not in ['2','6'] and x.count('7') <= 2]
print(len(b))
