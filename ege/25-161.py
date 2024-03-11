result = []
for N in range(150000000, 300000001):
    m = N
    n = 0
    while m % 2 == 0:
        m = m // 2
        n += 1
    if m == 1 and n % 2 == 1:
        result.append((N, n))
result.sort()
for N, n in result:
    print(N, n + 1)
