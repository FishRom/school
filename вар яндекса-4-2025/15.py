'''for a in range(0, 100):
    res = 1
    for x in range(1, 1000):
        for y in range(1, 1000):
            v = (-x**2 + 2*2*x - 4 + 3 < y) or ((x-1)**2 + y**2 < 7) or (5*x + a > y)
            if v == 0:
                res = 0
                break
        if res == 0:
            break
    if res == 1:
        print(a)
        break
'''
def f(a):
    for x in range(1, 500):
        for y in range(1, 500):
            z = ((-(x - 2)**2 + 3 < y) or ((x-1)**2 + y**2 < 7) or (5*x + a > y))
            if not z:
                return False
    return True

for a in range(-100, 300):
    if f(a):
        print(a)
        break
