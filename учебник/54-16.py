a = int(input())  #221
a1 = a % 10  #1
a //= 100 #2
f = 0
while a > 0:
    a2 = a % 10 #1
    a3 = a % 100 #21
    if a1 == a2 == a3:
        f += 1
    a //= 10 #22
    a1 = a2

if f > 0:
    print('correct')
else:
    print('wrong')
