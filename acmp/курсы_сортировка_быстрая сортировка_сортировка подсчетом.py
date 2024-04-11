n = int(input())
nums = list(map(int, input().split()))
c = []
def qsort(n, start, end):
    if start >= end:
        return None
    l = start
    r = end
    x = nums[(l + r) // 2]
    while l <= r:
        while nums[l] < x:
            l += 1
        while nums[r] > x:
            r -= 1
        if l <= r:
            nums[l],nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
    qsort(n, start, r)
    qsort(n, l, end)
    return nums
qsort(n, 0, len(nums) - 1)
print(*nums)

