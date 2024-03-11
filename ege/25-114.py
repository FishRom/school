def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_max_difference(start, end):
    max_difference = 0
    result_number = 0
    result_divisors = []
    for num in range(start, end + 1):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0 and is_prime(i) and is_prime(num // i):
                difference = abs(i - num // i)
                if difference > max_difference:
                    max_difference = difference
                    result_number = num
                    result_divisors = sorted([i, num // i])
    return result_divisors

start_num = 326359
end_num = 421986

result = find_max_difference(start_num, end_num)
print(*result)

#Valhalla Calling - Miracle of Sound