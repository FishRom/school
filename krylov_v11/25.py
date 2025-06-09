import fnmatch

for x in range(0, 10**9, 2049):
    if fnmatch.fnmatch(str(x), '32*21?4'):
        print(x, x//2049)