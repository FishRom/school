import itertools

val = '12 14 19 21 27 34 35 36 41 43 46 49 53 58 63 64 67 68 72 76 78 85 86 87 91 94'
row = 'аб ба бв вб ве ев ек ке ки ик иж жи жг гж га аг ад да бд дб еи ие ид ди дж жд'

for i in itertools.permutations('абвгдежик'):
    nval = val
    for j in range(len(i)):
            nval = nval.replace(str(j+1), i[j])

    if set(row.split()) == set(nval.split()):
        print('1 2 3 4 5 6 7 8 9')
        print(*i)