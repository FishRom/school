a = 16807**35 + 2401**2 * 343**9 - 49**52 + 7**3 - 2005
r = 0
while a > 0:
    if a % 49 > 9:
        r += 1
    a //= 49
print(r)