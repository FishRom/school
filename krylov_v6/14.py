for x in range(1, 23):
    a = int('200341011', 23) + x*23**6 + x*23**7 + int('22004', 23) + x*23**1 + int('11006', 23) + x*23**1
    if a % 22 == 0:
        print(x, a//22)



'''def f(n):
    res = ''
    while n > 0:
        res = str(n%23) + res
        n //= 23
    return res

for n in range(1, 23):
    if f()'''