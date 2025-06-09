import itertools

a = list(itertools.product('ФАВОРИТ', repeat=6))

a.sort()
b = [x for x in a if x[0] != 'О']
c = [x for x in b if x.count('Р') == 2]
v = []
for i in c:
    if c.index(i) % 2 == 0:
        #z = sum(c.index(i))
        v.append(i)
print(len(v))