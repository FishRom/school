import itertools

a = list(itertools.product('РЕПЛИКА', repeat=6))
a = [''.join(x) for x in a]
a.sort()
#print(a.index('РРРРРР'))
