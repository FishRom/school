def sum_cif(n, p):
    sum = 0
    while n > 0:
        sum += n % p
        n //= p
    return sum

n1, p1 = map(int, input().split())
n2, p2 = map(int, input().split())

if sum_cif(n1, p1) == sum_cif(n2, p2):
    print(sum_cif(n1, p1))
else:
    print(0)