import itertools

a = list(itertools.product('123456780', repeat=5))
a = [''.join(x) for x in a if x[0] != '0']

c = ['11', '22', '33', '44', '55', '66', '77', '88', '00']
b = [x for x in a if x.count('5') == 1 and sum(x.count(y) for y in c) == 0]
print(len(b))