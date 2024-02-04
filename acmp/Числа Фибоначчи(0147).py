'''f1 = 1
f2 = 1
a = int(input())
n = 0
while n < a - 2:
    fs = f1 + f2
    f1 = f2
    f2 = fs
    n += 1
print(f2)'''

'''n = int(input())
f1 = 1
f2 = 1
s = 0
if n == 1:
    s = 1
if n == 2:
    s = 2
for i in range(n - 2):
    fs = f1 + f2
    f2 = f1
    f1 = fs
    s += fs
print(f1)'''

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a + b
        return b

N = int(input("Введите номер числа Фибоначчи: "))
result = fibonacci(N)
print(f"{N}-е число Фибоначчи: {result}")