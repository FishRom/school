with open('17-3.txt', 'r') as file:
    sequence = [int(line.strip()) for line in file]

count = 0
max_sum = -88005553535

for i in range(len(sequence) - 1):
    if (sequence[i] % 2 == 0 and sequence[i] % 4 == 0 and sequence[i + 1] % 2 != 0 and sequence[i + 1] % 11 == 0) or \
       (sequence[i] % 2 != 0 and sequence[i] % 11 == 0 and sequence[i + 1] % 2 == 0 and sequence[i + 1] % 4 == 0):
        count += 1
        max_sum = max(max_sum, sequence[i] + sequence[i + 1])

print(count, max_sum)