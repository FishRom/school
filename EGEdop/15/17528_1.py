def p(x):
    return 15 <= x <= 40

def q(x):
    return 21 <= x <= 63

a=[]
for x in range(-21, 100):
    x += 0.5
    z = (p(x)) <= (((q(x) and (not(False))) <= (not(p(x)))))
    if z == 0:
        a.append(x)
print(len(a))