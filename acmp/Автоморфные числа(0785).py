def find_numbers_with_squares_endswith_itself(start, end):
    result = []
    for i in range(start, end + 1):
        kv = str(i ** 2)
        if kv.endswith(str(i)):
            result.append(i)
    return result

a, b = map(int, input().split())

result_list = find_numbers_with_squares_endswith_itself(a, b)

print(*result_list)