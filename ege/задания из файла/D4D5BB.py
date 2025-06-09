
def f2(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return i+n//i
    return 0

print(f2(20))
#print(sum(f(14)))
#print(f(900_002))
for x in range(900_001, 900_101):
    #print(f(x))
    if f2(x) % 10 == 8:
        print(x, f2(x))