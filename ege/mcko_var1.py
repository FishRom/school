#а остальные номера есть в тетради:D

'''
#№2
a = []
for i in range(1, 100):
    s = bin(i)[2:] #перевод во 2-ую систему счисления
    s = str(s)
    if s.count('1') % 2 == 0:
        s = "10" + s[2:] + '0'
    else:
        s = "1" + s[2:] + "01"
    r = int(s, 2) #перевод в десятичную систему счисления
    if r > 51:
        a.append(i)
print(min(a))
'''



'''определите количество трехзначных чисел в 
семиричной системе счисления, в записи которых не менее двух цифр 5'''
'''
#№6
from itertools import product
k = 0
a = '0123456'
s = list(product(a, repeat=3))    #вообще было написано после проверки, ранее была попытка сделать вручную
for i in s:
    i = ''.join(i)
    if i.count('5') >= 2 and i[0] != '0':
        k += 1
print(k)
'''

'''
#№5
a = []
for i in range(1, 100):
    s = bin(i)[2:]
    s = str(s)
    if s.count('1') % 2 == 0:
        s = "10" + s[2:] + '0'
    else:
        s = "1" + s[2:] + "01"
    r = int(s, 2)
    if r > 51:
        a.append(i)
print(min(a))
'''

#print(1092 - 782)

'''
#№10
s = '3' * 8 + '5' * 25
while '35' in s or '355' in s or '3555' in s:
    if '35'in s:
        s = s.replace('35', '3', 1)
    else:
        if '355' in s:
            s = s.replace('355', '3', 1)
        else:
            s = s.replace('3555', '5', 1)
print(s)
'''

'''
#№11
for x in range(11):
    s = int('253' + str(x) + '3', 11) + int('1' + str(x) + '365', 11)
    if s % 12 == 0:
        print(s // 12)
        break
'''


