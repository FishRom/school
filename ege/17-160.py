with open('17-3.txt', 'r') as file:
    numbers = [int(line.strip()) for line in file]

count = min_product = 0

for i in range(len(numbers) - 1):
    if numbers[i] * numbers[i + 1] > 0 and (numbers[i] + numbers[i + 1]) % 7 == 0:
        count += 1
        if count == 1 or numbers[i] * numbers[i + 1] < min_product:
            min_product = numbers[i] * numbers[i + 1]

print(count, min_product)