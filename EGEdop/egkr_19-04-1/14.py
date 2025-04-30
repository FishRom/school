def f(n):
    res = ''
    while n >0 :
        res = str(n%4) + res
        n //= 4
    return res

a = []
for x in range(1, 2001):
    a.append([f(4**210 + 4**110 - x).count('0'), x])

a.sort()
print(a)