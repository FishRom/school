def h (n):
    while n % 2 == 0:
        n //= 2
    while n % 5 == 0:
        n //= 5
    return n!= 1
a = int(input())
if h (a):
    print("YES")
else:
    print("NO")