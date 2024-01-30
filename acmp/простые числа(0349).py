n, m = map(int, input().split())
mas = [True] * (m + 1)
mas[0] = False
mas[1] = False
for i in range(2, int(m ** 0.5) + 1):
    if mas[i]:
        for j in range(i * i, m + 1, i):
            mas[j] = False
a = [i for i in range(n, m + 1) if mas[i]]
if not a:
    print('Absent')
else:
    print(*a, sep='\n')

#kdsknksdncsdcmsdncmdsnmdnvmsdnvsmdvnmsdvn
#dfghjkl;
