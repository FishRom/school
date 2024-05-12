'''for x in range(17):
    s = int('66' + str(x) + '63', 17) - int('5' + str(x) + '810', 17)
    if s % 11 == 0:
        print(s // 11)
        break'''


from itertools import product

k = 0
#a = '012'
#s = list(product(a, repeat=6))
for a in product("0123456789AB", repeat=3):
    s = ''.join(a)
    if s[0] != '0':
        if s.count("2") == 1:
            q = s.replace("0", "x")
            #q = q.replace("2", "x")
            if "x2" in q:
                k += 1
print(k)