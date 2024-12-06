'''import itertools

a = list(itertools.product('РЕКОГНОСЦИРОВКА', repeat=21))
#print(a)
a = [''.join(x) for x in a if x.count('Е') == 1 and x.count('О') == 3 and x.count('И') == 1 and x.count('А') == 1]
#print(a)

b = [x for x in a if x.index('A') + x.index('Е') + x.index('О') + x.index('И') == 21]
print(len(b) + 1)'''
print(120*(7**15))