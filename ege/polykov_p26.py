
for x in range(15):
    a = int('12305', 15) + x * 15**1 + int('10233', 15) + x * 15**3
    if a % 14 == 0:
        for x in range(15):
            a = int('12305', 15) + x * 15**1 + int('10233', 15) + x * 15**3
    if a % 14 == 0:
        print(a // 14, x)