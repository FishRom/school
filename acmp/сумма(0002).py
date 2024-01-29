n = int(input())
if n > 0:
    s = (n * (n + 1)) // 2
    print(s)
else:
    s = ((-n) * (-n + 1)) // (-2)
    print(s)