import itertools

a = list(itertools.permutations('123450', r=6))
a = [''.join(x) for x in a if x[0] != '0']

b = [x for x in a if x.count('0') == 1]
c = [x for x in b if '01' not in x and '03' not in x and '05' not in x and '10' not in x and '30' not in x and '50' not in x]
print(c)
print(len(c))