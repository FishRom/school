import itertools

a = list(itertools.product('01234', repeat=3))
a = [''.join(x) for x in a if x[0] != '0']
print(a)
b = [x for x in a if x[0] > x[1] > x[2]] #???
print(len(b))