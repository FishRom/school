count = 0
max_number_starting_with_50 = None


for num in range(1007, 746002):
    m = max(map(int, str(num)))
    first_digit = int(str(num)[0])
    if first_digit == m:
        count_of_5s = str(num).count('5')
        if count_of_5s >= 2 and count_of_5s % 2 == 0:
            count += 1
            if str(num).startswith('50'):
                max_number_starting_with_50 = num

print(count, max_number_starting_with_50)