sequence = [int(x) for x in open("17-3.txt")]

count = 0
min_sum = float('inf')

for i in range(len(sequence) - 3):
    if sequence[i] > sequence[i+1] > sequence[i+2] > sequence[i+3] and abs(sequence[i] - sequence[i+3]) > 1000:
        count += 1
        current_sum = sum(sequence[i:i+3])
        if current_sum < min_sum:
            min_sum = current_sum

print(count, min_sum)
