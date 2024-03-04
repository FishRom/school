def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def has_smallest_digit(n):
    digits = [int(digit) for digit in str(n)]
    smallest = min(digits)
    first_three = digits[:3]
    return smallest not in first_three

numbers = []
for number in range(2020, 647039):
    digits_sum = sum(int(digit) for digit in str(number))
    digits = [int(digit) for digit in str(number)]
    min_digit = min(digits)
    first_three = digits[:3]

    if digits_sum < 10 and min_digit not in first_three:
        numbers.append(number)

if numbers:
    mean = sum(numbers) / len(numbers)
    closest_num = min(numbers, key=lambda x: abs(x - mean))
    count = len(numbers)
else:
    count = 0
    closest_num = 0

print(count, closest_num)
