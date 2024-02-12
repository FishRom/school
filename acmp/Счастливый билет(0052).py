ticket_number = input()

if len(ticket_number) != 6 or not ticket_number.isdigit():
    print("Неверный формат номера билета. Пожалуйста, введите 6 цифр.")
else:
    sum_first_half = sum(int(digit) for digit in ticket_number[:3])
    sum_second_half = sum(int(digit) for digit in ticket_number[3:])

    if sum_first_half == sum_second_half:
        print('YES')
    else:
        print("NO")