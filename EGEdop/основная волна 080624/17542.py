import itertools

row = 'ae ea de ed db bd bg gb gf fg fc cf ch hc ah ha hg gh eb be'
val = '13 18 25 28 31 34 36 43 46 52 57 63 64 67 75 76 78 81 82 87'

for i in itertools.permutations('abcdefhg'):
    nval = val
    for j in enumerate(i):
        nval = nval.replace(str(j[0] + 1), j[1])
    if set(row.split()) == set(nval.split()):
        print('1 2 3 4 5 6 7 8')
        print(*i)