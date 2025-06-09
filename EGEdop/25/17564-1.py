def f(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return n//i + i   #то бищь возвращаем непременно само М = сумму делителей числа
    return 0

for x in range(700_001, 700_101):
    m = f(x)
    if m % 10 == 4:
        print(x, m)