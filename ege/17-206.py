for i in '0123456789':
    for j in '0123456789':
        s = int(f'1{i}34567{j}9')
        if s % 17 == 0:
            print(s, s // 17)