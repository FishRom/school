for x in range(27):
    a = int('123024', 27) + x*27**2 + int('135078', 27) + x*27**2
    if a % 26 == 0:
        print(a // 26, x)