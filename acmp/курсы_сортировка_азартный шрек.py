carts = input().split()
sp = []
n = int(carts[0])
m = n // 2
carts = input().split()
for i in range(n):
    sp.append(int(carts[i]))

sp.sort()
sp.reverse()
summ_sh = 0
summ_kr = 0

for i in range(m):
    summ_sh += sp[i]

for i in range(m, n):
    summ_kr += sp[i]
    
ans = summ_sh - summ_kr
print(ans)