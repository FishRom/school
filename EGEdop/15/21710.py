def b(x):
    return 36 <= x <= 75

def c(x):
    return 60 <= x <= 110

a = []
for i in range(25, 120):
    x = i + 0.5
    z = (True) <= (b(x) == c(x))
    if not z:
        a.append(x)

print(max(a) - min(a) +1 )
print(a)
print(len(a))

