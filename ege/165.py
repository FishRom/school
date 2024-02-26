# Чтение данных из файла
f = [int(x) for x in open("17-3.txt", "r")]

# Функция для определения троек и их средних арифметических
triplets_count = 0
min_avg = []

# Проходим по последовательности, оставляя место для тройки элементов
for i in range(len(f) - 2):
    tri = f[i:i+3]
    # Проверяем условия для тройки элементов
    if all(num % 3 == 0 for num in tri) and \
    any(num % 12 == 0 for num in tri):
        triplets_count += 1
        min_avg.append(sum(f[i:i+3]) / 3)
    #all = возвращает True при всех True, иначе выдаст False
    #any = возвращает True при даже одном True, иначе выдаст False

#выводим результат
print(triplets_count, min(min_avg))

