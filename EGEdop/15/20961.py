def p(x):
    return 15 <= x <= 142

def q(x):
    return 38 <= x <= 167

x = []
for a in range(10, 200):
    a += 0.5
    z = (not( q(a) <= (( (True) and p(a) ) <= (not(q(a)))) ))
    if z == 1:
        x.append(a)
print(len(x))