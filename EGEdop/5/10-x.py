def f(n, x): #x = система счисления
    res = ''
    while n > 0:
        res = str(n % x) + res
        n //= x
    return res

print(f(51, 5))

a = '123456789'
print(a[-2:], a[2:])