def f(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return i + n//i
    return 0
#print(f(20))
for x in range(452_022, 452_082):
    if f(x) % 7 == 3:
        print(x, f(x))