def f(n):
	res = ''
	while n > 0:
		res = str(n%5) + res
		n //= 5
	return res
	
a = f(5**2022 - 2*5**1010 + 25**850 + 2500).count('4')
print(a)
