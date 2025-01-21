def b(x):
    return 70 <= x <= 90
def f(a):
    for x in range(1, 1000):
        z = (x % a == 0) or (b(x) <= (x%22 != 0))
        if not z:
            return False
    return True


for a in range(1, 500):
    if f(a):
        print(a)