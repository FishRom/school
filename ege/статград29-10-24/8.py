import itertools

a = list(itertools.product('0123456789ABCDE', repeat=8))
a = [''.join(x) for x in a if x[0] != '0']

b = ['A', 'B', 'C', 'D', 'E']
c = [x for x in a if x.count('0') == 2 and sum(x.count(y) for y in b) <= 4]
print(len(b))

#ответ: 28642760