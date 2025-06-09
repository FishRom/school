def t(a, b, c):
    return a + b > c and a + c > b and b + c > a
a = 100
while True:
    z = ((not((t(x, 12, 20) == (not(max(x, 5)) > 28)) and t(x, a, 3))) for x in range(1, 1000))
    if all(z):
        print(a)
        break
    a -= 1