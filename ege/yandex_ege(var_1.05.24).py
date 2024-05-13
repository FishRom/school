'''from itertools import product
k = 0
f = 9
for a in product("01", repeat=f - 1):
    s = ''.join(a)
    if len(set(s)) != 1:
        k += 1
n = (10 ** (f - 1) - k * 9 - 9) * 9 - 9
print(n)'''

k=0
for x1 in '1234567':
    for x2 in "01234567":
        for x3 in "01234567":
            for x4 in '01234567':
                for x5 in "01234567":
                    s = x1 + x2 + x3 + x4 + x5
                    if s.count ('1')==0:
                        if s.count(x1) == 1 and s.count(x2) == 1 and s.count(x3) == 1 and  s.count(x4) == 1 and s.count(x5) == 1:
                            if x1:
                                pass