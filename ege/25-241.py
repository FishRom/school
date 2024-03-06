count = 0
for i in range(1, 10 ** 7):
    if i % 6 == 0 and i % 7 == 0 and i % 8 == 0:
        s = str(i)
        if s[1] + s[-2] == '66' and '6' in s[2:-2]:
            count += 1
            s = 0

            for d in range(1, i + 1):
                if i % d == 0:
                    s += d
            print(i, s)
            if count == 7:
                break