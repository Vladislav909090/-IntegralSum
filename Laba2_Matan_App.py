import tkinter as tk
import numexpr as ne
from math import *
import matplotlib.pyplot as plt
import random

# Создание окна приложения
root = tk.Tk()
root.geometry("640x250")
root.title("Построение графика функции")


def vertical_line(x, ylow, yhigh, line="--", clr="black", width=1):
    ax.plot([x, x], [ylow, yhigh], line, color=clr, linewidth=width)


def horizontal_line(xleft, xright, y, line="--", clr="black", width=1):
    ax.plot([xleft, xright], [y, y], line, color=clr, linewidth=width)


# Функция для построения графика
def plot_graph():
    # ввод значений
    inputFunc = input_func.get()
    print(inputFunc)
    a, b = [float(i) for i in input_range.get().split()]
    print(a, b)
    n = int(input_n.get())
    print(n)
    typeInt_sum = typeInt_sumChoice.get()
    print(typeInt_sum)

    # в следующей части кода потенциально может возникнуть ошибка
    try:
        dx = round((b - a) / n, 10)

        y_values = []
        x_values = []
        i = a - (b - a) * 0.05
        while i <= (b + (b - a) * 0.05):
            x_values.append(i)
            y_values.append(ne.evaluate(inputFunc.replace("x", "(" + str(i) + ")")))
            i += (b - a) / 2000

        # создание значений разбиений
        xn = []
        yn = []
        i = a
        while i <= b:
            xn.append(i)
            yn.append(ne.evaluate(inputFunc.replace("x", "(" + str(i) + ")")))
            i = round(i + dx, 10)
        # print(xn)

        points = []
        points_value = []
        # подсчет значений оснащений
        if typeInt_sum == "left":
            points = xn.copy()[:-1]
        elif typeInt_sum == "right":
            points = xn.copy()[1:]
        elif typeInt_sum == "medium":
            for i in range(len(xn) - 1):
                points.append((xn[i] + xn[i + 1]) / 2)
        elif typeInt_sum == "random":
            for i in range(len(xn) - 1):
                points.append(random.uniform(xn[i], xn[i + 1]))

        for i in points:
            points_value.append(ne.evaluate(inputFunc.replace("x", "(" + str(i) + ")")))

        Int_sum = dx * sum(points_value)
        print("Интегральная сумма - " + str(round(Int_sum, 10)))

        # дальше все график
        # Создание объекта графика
        global ax
        fig, ax = plt.subplots()

        # Добавление графика на графическую область
        ax.plot(x_values, y_values)
        vertical_line(a, 0, ne.evaluate(inputFunc.replace("x", "(" + str(a) + ")")), "--", "red", 2)
        vertical_line(b, 0, ne.evaluate(inputFunc.replace("x", "(" + str(b) + ")")), "--", "red", 2)
        # создание разбиений
        for i in range(1, len(xn) - 1):
            vertical_line(xn[i], 0, yn[i], "--", "green", 1)
        # создание оснащений
        for i in range(len(points)):
            plt.scatter(points[i], points_value[i], s=25, c="red", marker="*")
        # создание участков по оснащениям
        vertical_line(xn[0], 0, points_value[0], "-", "purple", 1)
        vertical_line(xn[-1], 0, points_value[-1], "-", "purple", 1)
        for i in range(len(xn) - 2):
            horizontal_line(xn[i], xn[i + 1], points_value[i], "-", "purple", 1)
            vertical_line(xn[i + 1], points_value[i], points_value[i + 1], "-", "purple", 1)
        horizontal_line(xn[-2], xn[-1], points_value[-1], "-", "purple", 1)

        # Настройка заголовка и меток осей, создание оси OX
        ax.axhline(y=0, color='k')
        ax.set_xlabel('Метка оси X')
        ax.set_ylabel('Метка оси Y')
        ax.set_title("y = " + inputFunc + "\nИнтегральная сумма - " + str(round(Int_sum, 10)))

        # Отображение графика
        plt.show()
    except:
        close_and_error()


def close_and_error():
    root.destroy()
    new_root = tk.Tk()
    new_root.geometry("200x50")
    label = tk.Label(new_root, text="Что-то пошло не так")
    label.pack()
    new_root.mainloop()


# Создание поля ввода для функции
label_func = tk.Label(root, text="Введите функцию f(x), которая вас интересует:", font=("Arial", 10))
label_func.place(x=40, y=10)
input_func = tk.Entry(root, font=("Arial", 10), width=20)
input_func.place(x=450, y=10)

# Создание поля ввода для диапазона
label_range = tk.Label(root, text="Диапазон [a, b] (через пробел, дробную часть через точку): ", font=("Arial", 10))
label_range.place(x=40, y=50)
input_range = tk.Entry(root, font=("Arial", 10), width=20)
input_range.place(x=450, y=50)

# Создание поля ввода для количества разбиений
label_n = tk.Label(root, text="Сколько разбиений (n): ", font=("Arial", 10))
label_n.place(x=40, y=90)
input_n = tk.Entry(root, font=("Arial", 10), width=20)
input_n.place(x=450, y=90)

# Создание кнопок для выбора типа оснащения
label_type = tk.Label(root, text="Выберите вариант оснащения:", font=("Arial", 10))
label_type.place(x=40, y=130)
typeInt_sumChoice = tk.StringVar()
typeInt_sumChoice.set("medium")
button_left = tk.Radiobutton(root, text="left", font=("Arial", 10), variable=typeInt_sumChoice, value="left")
button_left.place(x=40, y=160)
button_right = tk.Radiobutton(root, text="right", font=("Arial", 10), variable=typeInt_sumChoice, value="right")
button_right.place(x=100, y=160)
button_medium = tk.Radiobutton(root, text="medium", font=("Arial", 10), variable=typeInt_sumChoice, value="medium")
button_medium.place(x=160, y=160)
button_random = tk.Radiobutton(root, text="random", font=("Arial", 10), variable=typeInt_sumChoice, value="random")
button_random.place(x=230, y=160)

button = tk.Button(root, text="Submit", command=plot_graph)
button.place(x=300, y=200)

root.mainloop()
