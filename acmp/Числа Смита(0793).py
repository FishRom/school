def is_smith_number(n):
    def sum_digits(n):
        return sum(int(d) for d in str(n))

    def prime_factors(n):
        i = 2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return factors

    if n < 4:
        return False

    prime_factors_sum = sum(sum_digits(f) for f in prime_factors(n))
    return prime_factors_sum == sum_digits(n)

numbers = list(map(int, input().split()))

for num in numbers:
    if is_smith_number(num):
        print(num)