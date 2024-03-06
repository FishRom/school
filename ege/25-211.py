d = int('79', 16)
h = '1234567890abcdef'
for i in h:
    for j in h:
        x = int('1' + i + 'ded' + j + 'ced', 16)
        if x % d == 0:
            print(x, x//d)