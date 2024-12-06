import itertools

a = list(itertools.product('123456780', repeat=5))
a = [''.join(x) for x in a if x[0] != '0']

b = ['11', '22', '00', '33', '44', '55', '66', '77', '88']
c = [x for x in a if x.count('5') == 1 and sum([x.count(y) for y in b]) == 0]
print(len(c))