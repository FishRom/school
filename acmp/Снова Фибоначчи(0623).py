def last_stifri():
    a, b = 0, 1
    res = []
    for i in range(60):
        a, b = b, a + b
        res.append(a % 10)
    return res


n = int(input())
res = last_stifri()
print(res[n % 60])