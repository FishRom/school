n = int(input("Введите стоимость покупки: "))

if n % 5 == 0:
    ans1 = int(n // 5)
    ans2 = 0
else:
    q = n // 5
    w = n - 5 * q
    while w % 3 != 0:
        w += 5
    ans1 = int((n - w) // 5)
    ans2 = int(w // 3)

print(ans1, ans2)

