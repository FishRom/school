import itertools

a = list(itertools.product('ПЛЮШКА', repeat=6))
a = [x for x in a]

a.sort()
b = [ x for x in a if len(set(x)) == 6 and x[0] != 'А']
a = [''.join(x) for x in a]
b = [''.join(x) for x in b]
a.sort()
b.sort()
print([(x, a.index(x)+1) for x in b[:10]])
#print(b[:20])

#КАЛПШЮ
#КЛАПШЮ