def f(n):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = r + '01'
    else:
        r = '1' + r + '1'
    return int(r, 2)
#print(f(12))
a = []
for n in range(1, 156):
    if f(n) > 156:
        a.append(n)
print(min(a))