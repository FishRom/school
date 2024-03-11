from fnmatch import fnmatch
#r = [0, 2, 4, 6, 8]
for i in range(257, 10 ** 11 + 1, 257):
    if fnmatch(str(i), '123[0, 2, 4, 6, 8]45?67') or fnmatch(str(i), '123[0, 2, 4, 6, 8][0, 2, 4, 6, 8]45?67') or \
        fnmatch(str(i), '123[0, 2, 4, 6, 8][0, 2, 4, 6, 8][0, 2, 4, 6, 8]45?67'):
        print(i, i // 257)