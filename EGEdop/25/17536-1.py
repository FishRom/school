def f(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            if (i + n//i)%10 == 4:
                return i + n//i
            else:
                break
    return 0

for x in range(800_001, 801_001):
    z = f(x)
    if z > 0:
        print(x, z)


