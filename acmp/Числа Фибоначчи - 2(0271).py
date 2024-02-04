# Функция для проверки, является ли число числом Фибоначчи
def is_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n

# Ввод числа от пользователя
n = int(input("Введите число: "))

# Проверка является ли число числом Фибоначчи
result = is_fibonacci(n)

if result:
    print("1")
    # Находим порядковый номер числа Фибоначчи
    a, b = 0, 1
    count = 1
    while b < n:
        a, b = b, a + b
        count += 1
    print(count)
else:
    print("0")
