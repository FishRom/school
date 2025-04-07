'''import itertools

a = list(itertools.permutations('1234560', r=6))
a = [''.join(x) for x in a if x[0] != '0']

b = [x for x in a if x.count('0') == 1]
c = [x for x in b if '02' not in x and '04' not in x and '06' not in x and '00' not in x and
     '20' not in x and '40' not in x and '60' not in x]
print(c)
print(len(c))'''
print((780*1024)/(10*1500))