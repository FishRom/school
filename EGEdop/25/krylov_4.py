def f(n):
    r = []
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            r.append(i)
            if i < n//i:
                r.append(n//i)
    #print(r)
    z = sum(r)
    if z % 10 == 5:
        return z
    else:
        return 0
#print(f(96))

for n in range(900_001, 900_101):
    z = f(n)
    if z > 0:
        print(n, z)