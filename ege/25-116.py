nums = []
count = 0
maks_dif = 0
for i in range(356738, 404321 + 1):
    f = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            f = False
    if f:
        count += 1
        nums.append(i)
    if len(nums) == 2 and nums[0] != nums[1]:
        dif = abs(nums[0] - nums[1])
        if dif > maks_dif:
            maks_dif = dif
            res = i
        #count += 1
        nums.append(i)
print(count, nums, sep="\n")


'''from sympy import primefactors

def find_numbers():
    numbers = []
    max_difference = 0
    result = 0

    for num in range(356738, 404322):
        factors = list(primefactors(num))
        if len(factors) == 2 and factors[0] != factors[1]:
            difference = abs(factors[0] - factors[1])
            if difference > max_difference:
                max_difference = difference
                result = num
            numbers.append(num)

    return len(numbers), result

count, number = find_numbers()
print(count)
print(number)'''