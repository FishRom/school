def f1(n):
    if n >= 0:
        if int(n ** 0.5)**2 == n:
            return True
    return False


with open('17var13.txt', 'r') as f:
    a = [int(x) for x in f]

    b = []
    for i in range(0, len(a) - 1):
        if [x for x in a[i:i+2] if f1(a[i]) or f1(a[i+1])]:
            b.append(sum(a[i:i+2]))
print(len(b), max(b))

