heads = int(input())
power = 3 ** (heads // 3)

if heads % 3 == 2:
    power *= 2
if heads % 3 == 1:
    power = power * 4 // 3

print(power)

#more power, more motivation