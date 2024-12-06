'''#33
import itertools

a = list(itertools.product('ПОРТ', repeat=5))
a = [''.join(x) for x in a]

a.sort()
b = a.index('ТОПОР')
c = a.index('РОПОТ')
print((b - c) + 1)'''

'''#88
import itertools

a = list(itertools.product('АИn', repeat=6))
a = [''.join(x) for x in a]

d = []
a.sort()
for x in a:
    if x[0] in 'АИ':
        d.append(a)
print(len(d))'''

'''#100
import itertools

a = list(itertools.permutations('ПАНЕЛЬ', r=6))
a = [''.join(x) for x in a]

b = [x for x in a if x[0] != 'Ь']
c = [x for x in b if x.count('ЕАП') == 0]
print(len(c))'''

#156
'''import itertools

a = list(itertools.permutations('1234567890', r=5))
a = [''.join(x) for x in a if x[0] != '0']
#print(a)


b = [x for x in a if int(x) % 5 == 0]
g = 0
for i in b:
    n = i.replace('2', 'Ч').replace('4', 'Ч').replace('6', 'Ч').replace('8', 'Ч')\
        .replace('0', 'Ч').replace('1', 'Н').replace('3', 'Н').replace('5', 'Н')\
        .replace('7', 'Н').replace('9', 'Н')
    #print(n[:10])
    #print(n)
    if 'НН' not in n and 'ЧЧ' not in n:
        print(n)
        g += 1
print(g)'''

#166
'''import itertools

a = list(itertools.permutations('1234567890ABCDEF', r=5))
a = [''.join(x) for x in a if x[0] != '0']

#b = [x for x in a if int(x) % 5 == 0]
g = 0
for i in a:
    n = i.replace('2', 'Ч').replace('4', 'Ч').replace('6', 'Ч').replace('8', 'Ч')\
        .replace('0', 'Ч').replace('1', 'Н').replace('3', 'Н').replace('5', 'Н')\
        .replace('7', 'Н').replace('9', 'Н').replace('A', 'Ч').replace('B', 'Н') \
        .replace('C', 'Ч').replace('D', 'Н').replace('E', 'Ч').replace('F', 'Н')
    #print(n[:10])
    #print(n)
    if 'НН' not in n and 'ЧЧ' not in n:
        print(n)
        g += 1
print(g)'''

#230
'''import itertools

a = list(itertools.product('123456780', repeat=7))
a = [''.join(x) for x in a if x[0] != '0' and x[0] != '3' and x[0] != '7']

c = [x for x in a if '00' not in a and '11' not in a and '22' not in a and '33' not in a and '44' not in a and '55' not in a and \
     '66' not in a and '77' not in a and '88' not in a]
print(len(c))'''

#231
'''import itertools

a = list(itertools.product('123456780', repeat=7))
a = [''.join(x) for x in a if x[-1] != '0' and x[-1] != '3' and x[-1] != '7' and x[-1] != '4']

c = [x for x in a if '000' not in a and '111' not in a and '222' not in a and '333' not in a and '444' not in a and '555' not in a and \
     '666' not in a and '777' not in a and '888' not in a]
print(len(c))'''

#240
'''import itertools

a = set(itertools.permutations('АКАРИДА', r=7))
a = [''.join(x) for x in a if x.count('А') == 3 and x.count('К') == 1 and x.count('Р') == 1 and x.count('И') == 1 and x.count('Д') == 1]
#print(a)

g = 0
for i in a:
    n = i.replace('К', 'S').replace('Р', 'S').replace('Д', 'S').replace('А', 'G')\
            .replace('И', 'G')
    #print(n)
    if 'GG' not in n and 'SS' not in n and 'GGSS' not in n and 'SSGG' not in n:
        print(i, n)
        g += 1
print(g)  #мы стввим здесь set дабы избежать повторов слов по типу "иракада иракада". но эт пиздец
'''
#383
import itertools

a = set(itertools.product('0123456', repeat=5))
a = [''.join(x) for x in a if x[0] != '0']
print(len(a))
