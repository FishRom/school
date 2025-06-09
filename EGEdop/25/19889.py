def f(n):
    r = []
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            r.append(i)
            if i < n//i:
                r.append(n//i)
    return min([x for x in r if x > 5 and x % 10 == 5], default=0)

for n in range(902715, 902915):
    if f(n) > 0:
        print(n, f(n))