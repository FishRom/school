#2
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                a = (y and (x or z) or (not(y or z)) or w)
                if not a:
                    print(x, y, w, z)

#8

'''import itertools

a = list(itertools.product('123456780', repeat=5))
a = [''.join(x) for x in a if x[0] != '0']

b = ['11', '22', '33', '44', '55', '66', '77', '88', '00']
c = [x for x in a if x.count('5') == 1 and sum(x.count(y) for y in b) == 0]

print(len(c))'''

#14

'''a = 2 * 729**333 + 2 * 243**334 - 81**335 + 2 * 27**336 - 2 * 9**337 - 338
r = 0
while a > 0:
    if a % 9 > 0:
        r += 1
    a //= 9
print(r)'''

#15

'''for a in range(0, 100):
    r = 1
    for x in range(0, 1000):
        z = ((x & a == 0) or (not(x & 37 == 0)) or (not(x & 12 == 0)))
        if z == 0:
            r = 0
            break
    if r == 1:
        print(a)'''

#16

'''import sys

sys.setrecursionlimit(5000)
def f(n):
    if n <= 3:
        return 1
    else:
        return (n+3)*f(n-2)
print(f(2028)/f(2024))'''

#19-21

'''def f(n1, st, mst):
    if st > mst:
        return False
    if n1 >= 301:
        return st % 2 == mst % 2

    #new move
    st += 1
    a = []
    a.append(f(n1 + 3, st, mst))
    a.append(f(n1 * 5, st, mst))

    if st % 2 == mst % 2:
        return any(a)
    else:
        return all(a)

for n in range(1, 301):
    for mst in range(1, 5):
        if f(n, 0, mst):
            if mst == 4:
                print(n, mst)
            break'''
