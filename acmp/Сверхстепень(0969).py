n, m = map(int, input().split())

# Вычисляем 2 в степени n по модулю m
res = pow(2, pow(2, n), m) #pow(base, exp)
                            #base - возводимое число,
                            #exp - число, являющееся степенью,
print(res)
