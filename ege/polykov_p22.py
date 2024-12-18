'''def f1(n):
    r = ''
    while n > 0:
        r = str(n % 3) + r
        n //= 3
    return r

print(f1(9**8+3**5-9))'''

#p-21

a = bin(4**512 + 8**512 - 2**128 - 250)[2:]
print(a.count('0'))
