'''
#number 3
На вход алгоритма подается натуральное число N > 1. Алгоритм строит по
нему новое число R следующим образом.
1. Строится двоичная запись числа N.
2. Из полученной записи убирается старшая (левая) единица.
3. Далее эта запись обрабатывается по следующему правилу:
a) если в полученной записи количество единиц четное, то слева
дописывается 10;
b) если количество единиц нечётное, слева дописывается 1, справа 0.
Полученная таким образом запись является двоичной записью искомого
числа R.
Например, для исходного числа 4 = 1002 результатом будет являться число
8 = 10002, а для исходного числа 6 = 1102 результатом будет являться число
12 = 11002.
Укажите максимальное число R, меньшее 450, которое может являться
результатом работы алгоритма. В ответе запишите это число в десятичной
системе счисления.'''

'''ans = 0
for i in range(449, -1, -1):
    s = bin(i)[2:] #перевод во 2-ую систему счисления
    s = s[1:]
    if s.count('1') % 2 == 0:
        s = '10' + s
    else:
        s = "1" + s + '0'
    r = int(s, 2) #перевод в десятичную систему счисления
    if r < 450:
        ans = r if r > ans else ans
print(ans)'''




'''Сколько существует десятичных пятизначных чисел, содержащих в своей
записи ровно одну цифру 2, при этом рядом с этой цифрой могут стоять
только нечётные цифры?'''
#number 5
'''k = 0
from itertools import product
for a in product("0123456789", repeat=5):
    s = ''.join(a)
    if s[0] != '0':
        if s.count("2") == 1:
            q = s.replace("1", "x")
            q = q.replace("3", "x")
            q = q.replace("5", "x")
            q = q.replace("7", "x")
            q = q.replace("9", "x")
            if "x2x" in q or (s[0]=="2" and "2x" in q) or (s[-1]=='2' and "x2"in q):
                k += 1
print(k)'''

#number 8
'''s = '9' * 96
while '22222' in s or '9999' in s:
    if '22222' in s:
        s = s.replace('22222', '99', 1) #богом молю, пиши нормально, обозначая s =, иначе будет считать секстилион лет:_)
    else:
        s = s.replace('9999', '2', 1)
print(s)'''

#number 9
'''for x in '0123456789ABCDEFG':
    s = int('819' + str(x) + '6' + str(x) + '32', 17) + \
        int('45656925' + str(x), 17) + int('771377' + str(x) + '1', 17)
    if s % 16 == 0:
        print(s // 16)'''
