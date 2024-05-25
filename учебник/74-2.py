a = 0
b = 0
F = [1, 3, 6, 10]
l = [0.028, 0.070, 0.170, 0.260]
for i in range(1, len(F)):
    a = a + l[i] * l[i]
    b = b + l[i] * F[i]
k = b / a
print(k)
n = 1 / k
dl = []
for i in F:
    dl.append(i * n)
for i in range(1, len(F)):
    a = a + dl[i] * dl[i]
    b = b + dl[i] * F[i]
k2 = b / a
print(k2)