for i in '0123456789':
    for j in '0123456789':
        otvet = int(f'1{i}34567{j}9')
        if otvet % 17 == 0:
            print(otvet, otvet // 17)