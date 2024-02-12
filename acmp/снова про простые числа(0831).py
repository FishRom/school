
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def digit_sum(num):
    return sum(int(digit) for digit in str(num))

a, b = map(int, input().split())

max_sum = -1
max_number = -1
found_prime = False

for number in range(b, a - 1, -1):
    if is_prime(number):
        found_prime = True
        current_sum = digit_sum(number)
        if current_sum > max_sum or (current_sum == max_sum and number > max_number):
            max_sum = current_sum
            max_number = number

if found_prime:
    print(max_number)
else:
    print("В заданном диапазоне нет простых чисел.")