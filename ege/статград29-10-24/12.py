'''for s in range(123456794, 678901235):
    while 111 in s:
        s = s.replace(111, 2, 1)
        s = s.replace(222, 11, 1)
        s = s.replace(1, 2, 1)
print(s)'''

def replace(s, v, w):
    return s.replace(v, w, 1)

def process_string(n):
    s = '1' * n
    while '111' in s:
        s = replace(s, '111', '2')
        s = replace(s, '222', '11')
        s = replace(s, '1', '2')
    return s

count = 0
for N in range(123456794, 678901235):
    if process_string(N) == '2' * (N // 3):
        count += 1

print(count)

#бесконечные вычисления :/