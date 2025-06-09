def f(n, k):
	if n > k:
		return 0
	if n == k:
		return 1
	else:
		return f(n+ 2, k)+ f(n+7, k)

print(f(5, 49))
