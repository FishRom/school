a = int(input())  #221
a1 = a % 10  #1
a = a // 10 #22
f = 0
while a > 0:
    a2 = a % 10 #1
    if a1 == a2:
        f += 1
    a //= 10 #22
    a1 = a2

if f > 0:
    print('correct')
else:
    print('wrong')
