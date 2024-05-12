import matplotlib.pyplot as plt
a = 0
b = 10
eps = 0.001
def optimal_cut(a, b, eps, k):
    steps = 0
    delta = 2 * eps
    while b - a > delta:
        steps += 1
        r = k * (b - a)
        x1 = (a + b) / 2 - r
        x2 = (a + b) / 2 + r
        if f(x1) > f(x2):
            a = x1
        else:
            b = x2
    x = (a + b)/2
    return steps, x
def f(x):
    return x ** 2 - 4 * x + 4


k_values = [0.00001, 0.0001, 0.001, 0.01, 0.1]
steps_list = []

for k in k_values:
    steps, r = optimal_cut(a, b, eps, k)
    steps_list.append(steps)
    print(f'Для k={k}, количество шагов: {steps} ')
    print(r)

plt.plot(k_values, steps_list, marker='o')
plt.title('Зависимость количества шагов от k')
plt.xlabel('Значение k')
plt.ylabel('Количество шагов')
plt.grid(True)
plt.show()