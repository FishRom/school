def b(x):
    return 15 <= x <= 40

def c(x):
    return 21 <= x <= 63


a = []
for i in range(1, 100):
    i += 0.5
    z = ((not(b(i))) <= (((c(i)) and (True)) <= (b(i))))
    if not z:
        a.append(i)

print(max(a) - min(a) + 1)