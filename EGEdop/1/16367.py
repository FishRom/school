import itertools

val = '12 14 16 21 26 35 37 41 45 53 54 57 61 62 67 73 75 76'
row = 'ag ga bg gb be eb ef fe fd df dc cd ca ac ba ab fc cf'

for i in itertools.permutations('agbefdc'):
    nval = val
    for j in range(len(i)):
        nval = nval.replace(str(j + 1), i[j])
    if set(row.split()) == set(nval.split()):
        print('1 2 3 4 5 6 7')
        print(*i)