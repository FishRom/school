def f(a):
    for x in range(0, 400):
        for y in range(0, 400):
            z = (5 < y) or (x > 32) or (x + 2*y < a)
            if not z:
                return False
    return True

for n in range(0, 400):
    if f(n):
        print(n)
        break