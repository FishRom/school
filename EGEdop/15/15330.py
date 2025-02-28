def b(x):
    return 24 <= x <= 90

def c(x):
    return 47 <= x <= 115

a = []
for i in range(15, 125):
    x = i + 0.5
    z = (c(x)) <= (((True) and b(x)) <= (not(c(x))))
    if not z:
        a.append(x)
print(len(a))