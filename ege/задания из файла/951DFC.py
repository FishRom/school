def f(a):
    for x in range(1, 100):
        for y in range(1, 100):
            z = (99 != y + 2*x) or (a < x) or (a < y)
            if not z:
                return False
    return True

v = []
for a in range(1, 100):
    if f(a):
        v.append(a)
print(max(v) - min(v) + 1)