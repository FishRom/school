def calculate_fac(num, f):
    n = int(num)
    fak_length = len(f)
    res = 1
    for i in range(n, 0, -fak_length):
        res *= i
    return res


numb, kolva = map(str, input().split())
res = calculate_fac(numb, kolva)
print(res)