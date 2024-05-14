'''Сколько существует девятеричных шестизначных чисел, содержащих
в своей записи ровно одну цифру 4, при этом рядом с этой цифрой
могут стоять только чётные цифры?'''
'''k = 0
from itertools import product
for a in product("012345678", repeat=6):
    s = ''.join(a)
    if s[0] != '0':
        if s.count("4") == 1:
            q = s.replace("0", "x")
            q = q.replace("2", "x")
            q = q.replace("6", "x")
            q = q.replace("8", "x")
            if "x4x" in q or (s[0] == "4" and "4x" in q) or (s[-1] == '4' and "x4" in q):
                k += 1
print(k)'''



#########



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