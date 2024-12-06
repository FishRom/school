#готовая 1 задачка("Выясните, какое количество троек чисел может являться углами тупоугольного треугольника.")

with open('9_1.csv', 'r') as f:
    r = 0
    for i in f:
        a = [int(x) for x in i.split(';')]
        a.sort()
        #b = [x for x in a if sum(a) == 180 and a[0] + a[1] > 90]
        if sum(a) == 180 and a[0] + a[1] < 90:
            r += 1
print(r)#1071




