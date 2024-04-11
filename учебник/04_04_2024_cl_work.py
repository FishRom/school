'''n = int(input('Введите число строк(n) '))
m = int(input('Введите число столбцов(m) '))
for j in range(n):
        print(' '.join([str(i + 1 + m * j) for i in range(m)][::pow(-1, j)]))'''


def spiralArray(n, m):
    tX = 0
    tY = 0
    bX = m - 1
    bY = n - 1
    k = 1
    array = [[0 for i in range(m)] for j in range(n)]
    while k <= n * m:
        x = tX
        y = tY
        for x in range(tX, bX + 1):
            array[y][x] = k
            k += 1
        tY += 1
        if k <= n * m:
            for y in range(tY, bY + 1):
                array[y][x] = k
                k += 1
            bX -= 1
        if k <= n * m:
            for x in range(bX, tX - 1, -1):
                array[y][x] = k
                k += 1
            bY -= 1
        if k <= n * m:
            for y in range(bY, tY - 1, -1):
                array[y][x] = k
                k += 1
            tX += 1
    return array

n = int(input())
m = int(input())
pic = spiralArray(n, m)
for r in pic:
    print(*r)