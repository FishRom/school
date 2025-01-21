def p(x):
    return 15<=x<=40

def q(x):
    return 21<=x<=63

a = []
for i in range(5, 80):
    x = i + 0.5
    z = (p(x) <= (((q(x) and (not(False))) <= (not(p(x))))))
    if not z:
        a.append(x)
print(len(a))