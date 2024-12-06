def q(x):
    return 1 <= x <= 42

def p(x):
    return 25 <= x <= 98

a = []
for x in range(-25, 100):
    x += 0.5
    z = (q(x) <= (((not(p(x))) and q(x)) <= (False)))
    if z == 0:
        a.append(x)
print(len(a))