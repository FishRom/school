#я правильно понмаю, что это никто не читает? тогда здесь можно писать всякую смешную фигню>:3
for i in range(244143, 367821 + 1):
    d = set()
    for j in range(1, int(i ** 0.5) + 1):
        if i % j == 0:
            d.add(j)
            d.add(i // j)
        if len(d) == 5:
            b = sorted(d)
            print(*b)