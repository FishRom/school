count = 0
maks = []
for i in range(3439, 7410):
    ab = i % 2
    ah = i % 6
    if ab != ah and (i % 9 or i % 10 or i % 11):
        count += 1
        maks.append(i)
print(count)
print(max(maks))
