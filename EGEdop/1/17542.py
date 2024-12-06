import itertools

val = '13 18 25 28 31 34 36 43 46 52 57 63 64 67 75 76 78 81 82 87'
row = 'de ed ea ae ah ha hc ch cf fc fg gf gb bg bd db eb be hg gh'

for i in itertools.permutations('aedbghcf'):
    nval = val
    for j in range(len(i)):
        nval = nval.replace(str(j + 1), i[j])
    if set(row.split()) == set(nval.split()):
        print('1 2 3 4 5 6 7 8')
        print(*i)