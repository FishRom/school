with open("INPUT.TXT", "r") as f:
    num = f.readline().strip()
with open("OUTPUT.TXT", "w") as f:
    f.write('1')
    for digit in reversed(num):
        if digit == '0':
            f.write('0')
        else:
            break