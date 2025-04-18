def p(x):
    return 17 <= x <= 58
def q(x):
    return 29 <= x <= 80

a = []
for x in range(10, 100):
    x += 0.5
    z = p(x) <= ((q(x) and (not(False))) <= (not(p(x))))
    if z == 0:
        a.append(x)
print(len(a))