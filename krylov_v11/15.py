def t(n, m, k):
    return n + m > k and n + k > m and m + k > n
a = 100
while True:
    if all((not((t(x, 11, 18) == (not(max(x, 5) > 15))) and t(x, a, 5))) for x in range(1, 100)):
        print(a)
        break
    a -= 1