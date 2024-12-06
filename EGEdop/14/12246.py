a = 2 * 729**333 + 2 * 243**334 - 81**335 + 2 * 27**336 - 2 * 9**337 - 338
r = 0
print(a)
while a > 0:
    if a % 9 > 0:
        r += 1
    a //= 9
print(r)
#print(len([x for x in str(a) if x != '0']))