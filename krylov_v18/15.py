def f(a):
    for x in range(1, 1000):
        z = (not(x % a == 0)) <= ((x % 26 == 0) <= (not(x % 169 == 0)))
        if not z:
            return False
    return True

for a in range(1, 1000):
    if f(a):
        print(a)