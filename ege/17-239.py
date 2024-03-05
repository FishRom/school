import fnmatch
def search(n):
    c = 0
    s = 0
    for i in range(2, n + 1, 2):
        if n % 1 == 0:
            s += i
            c += 1
    if c >= 4:
        return True, s
    return False, s

count = 0
start = 65000
while True:
    if fnmatch.fnmatch(str(start),'6*97*5'):
        a, b = search(start)
        if a:
            print(start, b)
            count += 1
        if count == 7:
            break
    start += 1