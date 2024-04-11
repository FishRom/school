n = int(input())
nums = list(map(int, input().split()))
id = 0
for i in range(n - 1, 0, -1):
    id, count = 0, nums[0]
    for j in range(1, i + 1):
        if count < nums[j]:
            id = j
            count = nums[j]
    print(id, end=' ')
    nums[id], nums[i] = nums[i], nums[id]
print('0', end=' ')