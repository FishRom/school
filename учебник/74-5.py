import numpy as np
from scipy.optimize import minimize

# Измеренные данные
t = np.array([0, 0.2, 0.4, 0.6, 0.8, 1])
y_measured = np.array([1, 2, 1.2, -0.6, -2, -1.5])

# Функция потерь
def loss(params):
    a, b, c = params
    y_predicted = a * np.sin(b * t + c)
    return np.sum((y_measured - y_predicted) ** 2)

# Начальные значения параметров
initial_guess = [1, 4, 1]

# Минимизация функции потерь
result = minimize(loss, initial_guess, method='Nelder-Mead')

# Оптимальные значения параметров
a_opt, b_opt, c_opt = result.x
print("Оптимальные значения параметров:")
print("a =", a_opt)
print("b =", b_opt)
print("c =", c_opt)