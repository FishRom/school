import sys

sys.setrecursionlimit(5000)

def f(n):
	if n <= 1:
		return 1
	if n % 2 != 0 and n > 1:
		return 5*n + f(n - 1) + f(2)
	if n % 2 == 0 and n > 1:
		return 3* f(n - 1)
		
print(f(23))
