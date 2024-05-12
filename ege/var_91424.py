'''#5

for i in range(1, 100):
    s = bin(i)[2:]
    if s.count('1') % 2 == 0:
        s += '00'
    else:
        s += '10'
    r = int(s, 2)
    if r > 77:
        print(r)
        break'''


'''#8
k = 0
from itertools import product
for a in product("012", repeat=6):
    s = ''.join(a)
    if s[0] != '0':
        if s.count("2") == 1:
            q = s.replace("0", "x")
            #q = q.replace("2", "x")
            if "x2" not in q:
                k += 1
print(k)'''

'''#12

s = '8' * 125
while '333' in s or '888' in s:
    if '333' in s:
        s = s.replace('333', '8', 1)
    else:
        s = s.replace('888', '3', 1)
print(s)'''


'''#14
for x in range(18):
    s = int('9009' + str(x), 18) + int('2257' + str(x), 18)
    if s % 15 == 0:
        print(s // 15)
        break'''