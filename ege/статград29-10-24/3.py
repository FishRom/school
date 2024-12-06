'''def f(n):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = '11' + r
    else:
        r = '1' + r + '10'

    return int(r, 2)

a = []
for n in range(234567890, 567891235):
    if f(n) < 567891234:
        a.append(n)
print(max(a))
'''

'''def max_result(N_start, N_end):
    max_R = 0
    for N in range(N_start, N_end + 1):
        # Получаем двоичную запись числа N
        binary_N = bin(N)[2:]  # Пропускаем '0b'

        if N % 2 == 0:  # Чётное
            new_binary = '11' + binary_N
        else:  # Нечётное
            new_binary = '1' + binary_N + '10'

        # Преобразуем обратно в десятичное число
        R = int(new_binary, 2)
        max_R = max(max_R, R)  # Находим максимум

    return max_R

# Задаем диапазон
N_start = 234567890
N_end = 587891234

# Получаем максимальное значение R
result = max_result(N_start, N_end)
print(result)'''
