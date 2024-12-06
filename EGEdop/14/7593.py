for x in range(15):
    a = int('97968013', 15) + x * 15**2 + int('70213', 15) + x * 15**3
    if a % 14 == 0:
        print(a // 14, x)