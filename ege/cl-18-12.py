import itertools

val = '13 16 17 25 26 28 31 38 45 48 52 54 57 61 62 67 71 75 76 82 83 84'
row = 'ae ea eh he hg gh gc cg fc cf af fa ed de df fd db bd bg gb hb bh'

for i in itertools.permutations('aedfhbgc'):
    nval = val
    for j in range(len(i)):
        nval = nval.replace(str(j + 1), i[j])

    if set(row.split()) == set(nval.split()):
        print('1 2 3 4 5 6 7 8')
        print(*i)