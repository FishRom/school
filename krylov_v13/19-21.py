def f(n1, n2, st, mst):
	if st > mst:
		return False
	if n1 * n2 >= 144:
		return st % 2 == mst % 2


	#new move
	a = []
	st += 1
	a.append(f(n1 + 1, n2, st, mst))
	a.append(f(n1 * 2, n2, st, mst))
	a.append(f(n1, n2 + 1, st, mst))
	a.append(f(n1, n2 * 2, st, mst))
	
	if st % 2 == mst % 2:
		return any(a)
	else:
		return all(a)
		

for n in range(1, 144):
	for mst in range(1, 5):
		if f(1, n, 0, mst):
			if mst == 4:
				print(n, mst)
