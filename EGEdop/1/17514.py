import itertools

val = '12 14 17 21 24 28 35 37 38 41 42 46 53 58 64 67 71 73 76 82 83 85'
row = 'ab ba ae ea ec ce cd dc df fd fh hf bh hb ah ha eg ge gf fg gc cg'

for i in itertools.permutations('abhfdcge'):
    nval = val
    for j in range(len(i)):
        nval = nval.replace(str(j + 1), i[j])

    if set(row.split()) == set(nval.split()):
        print(*i)