def count_digits(num):
    while num:
        digit = num % 10
        digits_count[digit] += 1
        num //= 10

def update_digits_count(i, j):
    i = 1
    while i < 10:
        j = 1
        while j < 10:
            c = (i * j)
            j += 1

# Считываем входные данные
N, M = map(int, input().split())
# Создаем массив для подсчета количества цифр от 0 до 9
digits_count = [0] * 10

# Считаем количество цифр в таблице умножения
for i in range(1, N + 1):
    for j in range(1, M + 1):
        update_digits_count(i, j)

# Выводим результат
for count in digits_count:
    print(count)
