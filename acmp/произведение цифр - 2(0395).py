l, r = map(int, input().split())
k = 0

for i in range(l, r+1):
    pr = 1
    a = i
    while a > 0:
        d = a % 10
        pr *= d
        a //= 10
    if pr != 0 and i % pr == 0:
        k += 0
print(k)