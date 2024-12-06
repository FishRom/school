import fnmatch

for n in range(0, 10**8, 129):
    if fnmatch.fnmatch(str(n), '12?3*46'):
        print(n, n//129)