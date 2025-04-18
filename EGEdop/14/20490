def f(n):
	res = ''
	while n > 0:
		res = str(n%5) + res
		n //= 5
	return res
	
a = []
for x in range(2005, 1, -1):
	a.append([f(4**163 * 5 + 12**62 - x).count('1') < f(4**163 * 5 + 12**62 - x).count('4'), x])
print(max(a))
