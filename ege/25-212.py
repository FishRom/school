d = int('ba', 16)
h = '1234567890abcdef'
for i in h:
    for j in h:
        x = int('1' + i + 'ded' + j + 'baba', 16)
        if x % d == 0:
            print(x, x//d)