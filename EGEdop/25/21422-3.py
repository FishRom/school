def f(n):
    a = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            a.append(i)
            a.append(n//i)
    return min([x for x in a if x > 7 and x % 10 == 7], default=0)

for x in range(1_125_001, 1_125_101):
    if f(x) > 0:
        print(x, f(x))