def kaprekar_constant(num):
    steps = 0

    while True:
        num_str = str(num).zfill(4)  # Дополнение числа лидирующими нулями до 4 цифр
        num_list = sorted(num_str, reverse=True)
        desc_num = int(''.join(num_list))
        asc_num = int(''.join(sorted(num_str)))
        diff = desc_num - asc_num

        if diff == num:  # Проверяем, достигли ли постоянной Капрекара
            return num, steps
        else:
            num = diff
            steps += 1

# Чтение входных данных
num = int(input())

# Получение результатов от функции и вывод
kaprekar, steps = kaprekar_constant(num)
print(kaprekar)
print(steps)
