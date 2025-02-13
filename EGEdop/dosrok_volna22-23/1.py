import itertools

row = 'АБ БА БВ ВБ ВГ ГВ ГЖ ЖГ ЖЕ ЕЖ ДЕ ЕД АД ДА БД ДБ ЕГ ГЕ'
val = '13 14 16 25 27 31 34 41 43 47 52 57 56 61 65 72 74 75' #цифры

for i in itertools.permutations('АБВГДЕЖ'):
    nval = val
    for j in range(len(i)):
        nval = nval.replace(str(j+1), i[j])

    if set(row.split()) == set(nval.split()):
        print('1 2 3 4 5 6 7')
        print(*i)