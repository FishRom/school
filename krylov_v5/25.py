import fnmatch

for x in range(0, 10**10, 31007):
    if fnmatch.fnmatch(str(x), '1*34?5?9'):
        print(x, x//31007)


