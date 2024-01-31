'''# Программа запрашивает у пользователя число N
n = int(input())

# Счетчик количества чисел, взаимно простых с N
count = 0

# Перебираем все числа меньше N
for i in range(1, n):
    # Находим наибольший общий делитель между N и текущим числом i
    f = True
    for j in range(2, min(n, i) + 1):
        if n % j == 0 and i % j == 0:
            f = False
            break

    # Если наибольший общий делитель равен 1, увеличиваем счетчик
    if f:
        count += 1

# Выводим результат
print(count)'''

n = int(input())

# Функция для нахождения наибольшего общего делителя
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

count = 0

# Перебираем возможные делители N
for i in range(1, n):
    if gcd(n, i) == 1:
        count += 1

print(count)