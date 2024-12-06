import itertools

val = '12 14 18 21 25 27 34 35 36 41 43 46 52 53 63 64 72 78 81 87'
row = 'fa af ae ea eb be bh hb hd dh dg gd gc cg cf fc ch hc ab ba'

for i in itertools.permutations('aebhdgcf'):
    nval = val
    for j in range(len(i)):
        nval = nval.replace(str(j + 1), i[j])

    if set(row.split()) == set(nval.split()):
        print('1 2 3 4 5 6 7 8')
        print(*i)