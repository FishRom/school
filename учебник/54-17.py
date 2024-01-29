a = input().split()
for i in a:
    if i[0] == i[-1]:
        print('right')
    else:
        print('wrong')