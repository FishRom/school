with open('17-3.txt', 'r') as file:
    sequence = [int(line.strip()) for line in file]

count = 0
min_avg = 1023849043580345803458034583458348000000

for i in range(len(sequence) - 1):
    product = sequence[i] * sequence[i + 1]
    avg = (sequence[i] + sequence[i + 1]) / 2

    if product % 2 != 0 and avg % 7 == 0:
        count += 1
        min_avg = min(min_avg, avg)

print(count, min_avg)