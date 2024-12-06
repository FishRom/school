import itertools

val = '14 17 18 23 28 32 35 36 41 45 53 54 63 67 71 76 78 81 82 87'
row = 'ag ga gd dg de ed ef fe fh hf bf fb bh hb bc cb cg gc ha ah'

for i in itertools.permutations('ahfedgbc'):
    nval = val
    for j in range(len(i)):
        nval = nval.replace(str(j + 1), i[j])

    if set(row.split()) == set(nval.split()):
        print('1 2 3 4 5 6 7 8')
        print(*i)