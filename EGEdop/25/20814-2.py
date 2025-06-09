def f(n):
    res = 0
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
           res += i
           if i < n//i:
               res += n//i
    return res

for x in range(500_001, 500_101):
    r = f(x)
    if r % 10 == 9:
        print(x, r)
