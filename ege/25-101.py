def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


maks = []
start = 125697
end = 190234

count = 0
for num in range(start, end + 1):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0 and is_prime(i) and is_prime(num // i):
            maks.append(num)
            count += 1
print(count, max(maks))
