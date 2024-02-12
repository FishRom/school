
def max_consecutive_numbers(num):
    max_count = 0
    count = 1

    while count * (count + 1) / 2 <= num:
        max_count = count
        count += 1

    return max_count


num = int(input("Введите натуральное число: "))
result = max_consecutive_numbers(num)

while result > 2:
    if num % result == 0:
        break
    result -= 1

print("Максимальное количество чисел в разложении:", result)