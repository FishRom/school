a = []
for x in range(0, 100):
    x += 0.5
    z = (17 <= x <= 58) <= (((29 <= x <= 80) and (True)) <= (not(17 <= x <= 58)))
    if z == 0:
        a.append(x)
print(len(a))