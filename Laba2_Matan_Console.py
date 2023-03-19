import matplotlib.pyplot as plt
import numpy as np

# Вводим количество разбиений и тип оснащения
n = int(input("Введите количество разбиений: "))
osn = input("Выберите тип оснащения (left, right, medium, random): ")

# Определяем отрезок и функцию
a, b = 1, 3
f = lambda x: np.exp(3*x) - 2*x

# Строим график функции
x_vals = np.linspace(a, b, 1000)
y_vals = f(x_vals)
plt.plot(x_vals, y_vals)

# Строим вертикальные пунктирные линии
x_points = np.linspace(a, b, n+1)
y_points = f(x_points)
for i in range(n):
    plt.plot([x_points[i], x_points[i]], [0, y_points[i]], linestyle='dashed', color='gray')

# Отмечаем точки в зависимости от выбранного типа оснащения
if osn == 'left':
    osn_vals = [f(x_points[i]) for i in range(n)]
elif osn == 'right':
    osn_vals = [f(x_points[i+1]) for i in range(n)]
elif osn == 'medium':
    osn_vals = [(f(x_points[i]) + f(x_points[i+1])) / 2 for i in range(n)]
else:
    osn_vals = [f(np.random.uniform(x_points[i], x_points[i+1])) for i in range(n)]

# Строим прямоугольники
for i in range(n):
    plt.fill_between([x_points[i], x_points[i+1]], [0, 0], [osn_vals[i], osn_vals[i]], alpha=0.3, color='blue')

# Отображаем график
plt.show()
