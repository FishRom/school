def f(n):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = '10' + r
    else:
        r = '1' + r + '01'
    return int(r, 2)

a = []
for n in range(1, 516):
    if f(n) > 516:
        a.append(n)
print(min(a))