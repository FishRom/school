def f(a):
    for x in range(1, 100):
        z = (not(x % a)) <= ((x % 54) <= (not(162 % x)))
        if not z:
            return False
    return True

for a in range(1, 100):
    if f(a):
        print(a)