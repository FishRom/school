'''from math import sqrt
a, b = map(int, input().split())
c = True
f = False
for i in range(a, b+1):
    f = True
    for j in range(2, int(sqrt(i)) + 1):
        if i % j == 0:
            f = False
    if f:
        print(i)
        c = False
if c:
    print('Absent')'''

'''n, m = map(int, input().split())
if n == 2:
    mylist = [2]
else:
    mylist = []
primes = [2]
now = 3
for now in range(3, m + 1, 2):
    for i in primes:
        if now % i == 0:
            break
        if i * i > now:
            primes.append(now)
            if now >= n:
                mylist.append(now)
                break
    now += 2
if mylist == []:
    print('Absent')
else:
    print(*mylist, sep='/n')'''

n, m = map(int, input().split())
mas = [True] * (m + 1)
mas[0] = False
mas[1] = True
flag = False
for i in range(m + 1):
    if mas[i]:
        if i >= n:
            print(i)
            flag = True
        for j in range(i + i, m + 1, i):
            mas[j] = False
if not flag:
    print('Absent')