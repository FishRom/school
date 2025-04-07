def f(a):
    res = ''
    while a > 0:
        res = str(a%7) + res
        a //= 7
    return res

a = []
for x in range(2030, 1, -1):
    #print(f(7**170 + 7**100 - x).count('0'))
    a.append([f(7**170 + 7**100 - x).count('0'), x])
print(max(a))
