import itertools

val = '12 15 16 21 23 24 32 36 37 42 47 51 56 61 63 65 73 74'
row = 'af fa fe ef ec ce cg gc gd dg db bd ab ba fb bf ed de'
for i in itertools.permutations('abdgcef'):
    nval = val
    for j in range(len(i)):
        nval = nval.replace(str(j + 1), i[j])

    if set(row.split()) == set(nval.split()):
        print(*i)
