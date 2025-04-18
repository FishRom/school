import fnmatch

for n in range(0, 10**10, 10980):
    if fnmatch.fnmatch(str(n), '20??22*'):
        print(n, n//10980)