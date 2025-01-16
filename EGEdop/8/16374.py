import itertools

a = list(itertools.product('1234560', repeat=7))
a = [''.join(x) for x in a if x[0] != '0']

chet = '2', '4', '6', '0'
b = [x for x in a if sum([x.count(y) for y in chet]) == 2]
print(b)
print(len(b))