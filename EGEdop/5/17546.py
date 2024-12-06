def f(n):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = '10' + r
    else:
        r = '1' + r + '01'
    return int(r, 2)

a = []
for n in range(1, 250):   #укажите максимальное число R
    if n < 12:
        a.append(f(n))
print(max(a))