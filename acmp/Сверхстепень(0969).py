n, m = map(int, input().split())

# Вычисляем 2 в степени n по модулю m
res = pow(2, pow(2, n), m)

print(res)
