for a in range(1, 100): #0 не является натуральным числом
    res = 1
    for x in range(1, 1000):
        z = ((x % 2 == 0) <= (x % 3 != 0)) or (x + a >= 80)
        if z == 0:
            res = 0
            break
    if res == 1:
        print(a)
        break