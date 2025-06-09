def p(x):
    return 15 <= x <= 40

def q(x):
    return 21 <= x <= 63

a = []
for x in range(5, 75):
    x = x + 0.5
    z = (p(x)) <= ((q(x) and (True)) <= (not(p(x))))
    if not z:
        a.append(x)
print(max(a) - min(a) + 1)
print(a)
print(len(a))