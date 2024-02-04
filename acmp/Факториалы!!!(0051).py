# Функция для вычисления факториала с двойным восклицательным знаком
def factorial_double_bang(n, k):
    result = 1
    if n % k == 0:
        for i in range(n, 0, -k):
            result *= i
    else:
        for i in range(n, 0, -k):
            if i <= 0:
                break
            result *= i
    return result

# Функция для проверки валидности ввода
def is_valid_input(s):
    return all(c.isdigit() or c == '!' for c in s)

# Получение входных данных
input_data = input()
n_str, k_str = input_data.split()

# Проверка валидности входных данных
if (n_str.isdigit() and k_str.count('!') == len(k_str) and 1 <= int(n_str) <= 10 and 1 <= len(k_str) <= 20):
    n = int(n_str)
    k = len(k_str)
    result = factorial_double_bang(n, k)
    print(result)
