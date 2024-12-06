import itertools

a = list(itertools.product('0123456789ABCD', repeat=5))
a = [''.join(x) for x in a if x[0] != '0']

c = ['B', 'C', 'D']
b = [x for x in a if x.count('9') == 1 and sum(x.count(y) for y in c) <= 3] #hdhdh
print(len(b))


