from fnmatch import fnmatch
#n = [1, 3, 5, 7, 9]
#ch = [0, 2, 4, 6, 8]
for i in range(92, 10 ** 8 + 1, 92):
    if fnmatch(str(i), "12[0, 2, 4, 6, 8]4[1, 3, 5, 7, 9]6?8"):
        print(i, i // 92)