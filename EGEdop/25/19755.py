def f(n):
    r = 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            r += i
            if i < n//i:
                r += n//i
    return r

for x in range(1_200_001, 1_201_001):
    if f(x) > 2000 and f(x) % 10 == 8:
        print(x, f(x))