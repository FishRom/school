def convert(n, base):
    if n == 0:
        return '0'
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    while n > 0:
        digit = n % base
        result = digits[digit] + result
        n //= base
    return result


count = 0
minimum = float('inf')
interesting_numbers = []

for i in range(1871, 9198):
    in_base_16 = convert(i, 16)
    in_base_10 = convert(i, 10)

    if len(in_base_16) != len(in_base_10) and (i % 9 == 2 or i % 9 == 3):
        count += 1
        minimum = min(minimum, i)
        interesting_numbers.append(i)

print(count, minimum)