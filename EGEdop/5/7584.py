def f(n):
    r = bin(n)[2:]
    if n % 3 == 0:
        r = r + r[-3:]
    else:
        r = r + bin(3 * (n % 3))[2:]
    return int(r, 2)
#print(f(9))
a = []
for n in range(1, 100):  #укажите наибольшее число N
    if f(n) < 100:
        a.append(n)
print(max(a))