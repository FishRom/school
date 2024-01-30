a, b = map(int, input().split())
last = a % 10
if b % 4 == 0:
    print((last ** 4) % 10)
else:
    print((last ** (b % 4)) % 10)