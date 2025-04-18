for x in range(21):
    a = int('8293402', 21) + x*21 + int('2924007', 21) + x*21 + x*21**2 + int('6756408', 21) + x*21
    if a % 20 == 0:
        print(x, a//20)

print(bin(224))
print(213//32)
print(6*32)