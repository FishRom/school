from math import sqrt

start = 478392
end = 502439


def is_prime(x):
    if x <= 1:
        return False
    for d in range(2, int(sqrt(x)) + 1):
        if x % d == 0:
            return False
    return True


min_diff = float('inf')
count = 0
i_min_diff = None

for i in range(start, end + 1):
    q = round(sqrt(i))
    divisors = [2] + [x for x in range(3, q + 1, 2)]

    for x in reversed(divisors):
        if i % x == 0 and is_prime(x):
            y = i // x
            if x != y and is_prime(y):
                count += 1
                if (y - x) < min_diff:
                    min_diff = y - x
                    i_min_diff = i
                break

print(count, i_min_diff)