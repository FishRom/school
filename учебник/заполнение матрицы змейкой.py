n = int(input()) #col
m = int(input()) #row
matrix = [[0 for i in range(n)] for i in range(m)]
num = 1

for col in range(n):
    if col % 2 == 0:
        for row in range(m):
            matrix[row][col] = num
            num += 1
    else:
        for row in range(m - 1, -1, -1):
            matrix[row][col] = num
            num += 1

for row in range(m):
    for col in range(n):
        print(matrix[row][col], end=" ")
    print()



'''a = input().split()
n, m = int(a[0]), int(a[1])
mat = []
for g in range(n):
    tap = [e for e in range(m)]
    mat.append(tap)

count = 1
for i in range(n):
    for j in range(m):
        mat[i][j] = count
        count += 1

for i in range(n):
    if i % 2 != 0:
        mat[i].reverse()

for i in range(n):
    for j in range(m):
        print(str(mat[i][j]).ljust(3), end=' ')
    print()'''
