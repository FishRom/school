def b(x):
	return 10 <= x <= 15
	
def c(x):
	return 20 <= x <= 27
	

for x in range(1, 30):
	res = 0
	z = (not((b(x) or c(x)) <= False))
	if z:
		print(x)
