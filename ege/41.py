result = []

for number in range(2371, 9433):
    if (oct(number)[-2:] == '15' or oct(number)[-2:] == '17') and number % 3 != 0 and number % 5 != 0:
        result.append(number)

print(len(result), max(result))