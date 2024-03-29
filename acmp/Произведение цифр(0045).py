# Запрашиваем у пользователя число n
n = int(input())

# Если n равно 0, то наименьшее число q не существует
if n == 0:
    print(-1)
else:
    # Инициализируем переменную q
    q = ""

    # Перебираем все возможные цифры от 9 до 2
    for i in range(9, 1, -1):
        # Пока n делится на i без остатка, добавляем i в начало строки q и делим n на i
        while n % i == 0:
            q = str(i) + q
            n //= i

    # Если после перебора цифр n не стало равным 1, значит Q не существует
    if n != 1:
        print(-1)
    else:
        # Преобразуем строку q в число и выводим его
        q = int(q)
        print(q)