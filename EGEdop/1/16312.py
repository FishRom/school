import itertools

val = '13 17 25 27 31 34 37 43 47 52 56 65 67 71 72 73 74 76'
row = 'ac ca ag ga cd dc gd dg db bd de ed ef fe bf fb ad da'

for i in itertools.permutations('acgdbfe'):
    nval = val
    for j in range(len(i)):
        nval = nval.replace(str(j + 1), i[j])
    if set(row.split()) == set(nval.split()):
        print('1 2 3 4 5 6 7')
        print(*i)