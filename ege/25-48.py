
lst = []
for i, num in enumerate(range(2484292, 2484370 + 1), start=1):
    f = True
    if num <= 1:
        f = False
    for j in range(2, int(num ** 0.5) + 1):
        if num % j == 0:
            f = False
            break
    if f:
        lst.append((i, num))
count = 0
for num in lst:
    count += 1
    print(f"{count} {num[1]}", sep='\n')

'''start_num = 2484292
end_num = 2484370
prime_numbers = []

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for i, num in enumerate(range(start_num, end_num + 1), start=1):
    if is_prime(num):
        prime_numbers.append((i, num))
count = 0
for num in prime_numbers:
    count += 1
    print(f"{count} {num[1]}", sep='\n')'''