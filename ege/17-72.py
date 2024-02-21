count = 0
largest_starting_with_8 = 0

for num in range(2848, 109500):
    if '9' in str(num):
        digit_sum = sum(int(digit) for digit in str(num) if int(digit) > 5)
        if digit_sum % 3 == 0:
            count += 1
            if str(num).startswith('8'):
                largest_starting_with_8 = num

print(count, largest_starting_with_8)