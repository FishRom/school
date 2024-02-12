
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_2_prime(num):
    str_num = str(num)
    increasing_order = int("".join(sorted(str_num)))
    decreasing_order = int("".join(sorted(str_num, reverse=True)))

    return is_prime(increasing_order) and is_prime(decreasing_order)


n1 = int(input())
if is_2_prime(n1):
    print("Yes")
else:
    print("No")
