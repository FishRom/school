def f(a):
    for x in range(0, 5000):
        z = ((not(x % a == 0)) and (x % 35 == 0)) <= ((not(x % 21 == 0)) or (not(x % 35 == 0)))
        if not z:
            return False
    return True

for a in range(1, 300):
    if f(a):
        print(a)