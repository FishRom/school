import itertools

a = list(itertools.product('ЛАЙМ', repeat=5))
a = [''.join(x) for x in a]
a.sort()

b = [x for x in a if x.count('М') == 0 and x.count('Л') == 0]
c = [x for x in b if x.count('ЙЙ') == 0]
c.sort()
print(c)
print(a.index('ЙАЙАЙ') + 1)