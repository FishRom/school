from math import sqrt
start_number, end_number = 158928, 345293

def is_prime(number):
    if number <= 1:
        return False
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1
    return True


count = 0
minimum_number = 0

for i in range(start_number, end_number + 1):
    square_root = round(sqrt(i))
    divisors = [2] + list(range(3, square_root + 1, 2))
    found = False
    for divisor in divisors:
        if i % divisor == 0 and is_prime(divisor):
            quotient = i // divisor
            quotient_square_root = round(sqrt(quotient))
            for y in range(divisor + 1, quotient_square_root + 1):
                if quotient % y == 0 and is_prime(y):
                    z = quotient // y
                    found = True
                    if z != y and z != divisor and is_prime(z):
                        count += 1
                        if minimum_number == 0:
                            minimum_number = i
                    break
            if found:
                break
print(count, minimum_number)