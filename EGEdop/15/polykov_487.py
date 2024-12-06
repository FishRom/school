def p(x):
    return 5 <= x <= 20

def q(x):
    return 15 <= x <= 25

def r(x):
    return 35 <= x <= 50

a = []
for x in range(-20, 100):
    x += 0.5
    z = ((p(x) <= q(x)) or ((True) <= (not(r(x)))))
    if z == 0:
        a.append(x)
print(len(a))