def f(n):
    r = []
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            if (n//i - i)%100 == 30:
                return n//i - i
            else:
                return 0
    return 0

for x in range(860_001, 861_001):
    z = f(x)
    if z > 0:
        print(x, z)