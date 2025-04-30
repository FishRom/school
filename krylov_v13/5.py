def f(n):
    r1 = (n//100)**2 + ((n//10)%10)**2
    #print(r1)
    r2 = ((n//10)%10)**2 + (n % 10)**2
    #print(r2)
    if r1 > r2:
        r = str(r1) + str(r2)
    else:
        r = str(r2) + str(r1)
    return r
print(f(946))
#print(621%10)
#print((621//10)% 10)
#print(621//100)
'''for x in range(100, 1000):
    if f(x):
        print(f(x), x)
'''