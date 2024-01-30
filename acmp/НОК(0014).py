a, b = map(int, input().split())
c = a * b
while a > 0 and b > 0:
    if a >= b:
        a %= b
    else:
        b %= a
nod = a + b
print(c // nod)