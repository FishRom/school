def f1(x, y):
    if x == y:
        return 1
    elif x > y:
        return 0
    else:
        return f1(x + 1, y) + f1(x + 2, y) + f1(x + 3, y)

print(f1(5, 7)*f1(7, 11))