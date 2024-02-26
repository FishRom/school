a = [int(x) for x in open('17-3.txt')]

count = 0
min_difference = float('inf')

for i in range(len(a) - 2):
    if a[i] < a[i + 1] < a[i + 2]:
        count += 1
        difference = a[i + 2] - a[i]
        if difference < min_difference:
            min_difference = difference

print(count, min_difference)