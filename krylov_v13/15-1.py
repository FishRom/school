def b(x):
    return 10 <= x <= 15

def c(x):
    return 20 <= x <= 27
q = []
for a in range(1, 30):
    a += 0.5
    z = ((b(a) or c(a)) <= (False))
    if not z:
        q.append((a))
        print(a)
print(max(q) - min(q) +1)