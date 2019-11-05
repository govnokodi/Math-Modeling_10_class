import numpy as np
import matplotlib.pyplot as plt

#график линия 
plt.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) # поле
plt.show()


#график ломаная 
plt.plot([1, 7, 3, 5, 11, 1]) #точки на поле 
plt.show()


# Независимая (x) и зависимая (y) переменные
x = np.linspace(0, 10, 50)
y = x
# Построение графика
plt.title("Линейная зависимость y = x") # заголовок
plt.xlabel("x") # ось абсцисс
plt.ylabel("y") # ось ординат
plt.grid(True)      # включение отображение сетки
plt.plot(x, y, "r--")  # построение графика
plt.show()


# Линейная зависимость
x = np.linspace(0, 10, 50)
y1 = x
# Квадратичная зависимость
y2 = [i**2 for i in x]
# Построение графика
plt.title("Зависимости: y1 = x, y2 = x^2") # заголовок
plt.xlabel("x")         # ось абсцисс
plt.ylabel("y1, y2")    # ось ординат
plt.grid(True)              # включение отображение сетки
plt.plot(x, y1, x, y2)  # построение графика
plt.show()


#Построение диаграммы для категориальных данных
fruits = ["apple", "peach", "orange", "bannana", "melon"]
counts = [34, 25, 43, 31, 17]
plt.bar(fruits, counts)
plt.title("Fruits!")
plt.xlabel("Fruit")
plt.ylabel("Count")
plt.show()


from matplotlib.ticker import (AutoMinorLocator)
x = np.linspace(0, 10, 10)
y1 = 4*x
y2 = [i**2 for i in x]
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_title("Графики зависимостей: y1=4*x, y2=x^2", fontsize=16)
ax.set_xlabel("x", fontsize=14)        
ax.set_ylabel("y1, y2", fontsize=14)
ax.grid(which="major", linewidth=1.2)
ax.grid(which="minor", linestyle="--", color="gray", linewidth=0.5)
ax.scatter(x, y1, c="red", label="y1 = 4*x")
ax.plot(x, y2, label="y2 = x^2")
ax.legend()
ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.tick_params(which='major', length=10, width=2)
ax.tick_params(which='minor', length=5, width=1)
plt.show()


#fg = plt.figure(figsize=(9, 9), constrained_layout=True)
#gs = fg.add_gridspec(5, 5)

#fig_ax_1 = fg.add_subplot(gs[0, :3])
#fig_ax_1.set_title('gs[0, :3]')

#fig_ax_2 = fg.add_subplot(gs[0, 3:])
#fig_ax_2.set_title('gs[0, 3:]')

#fig_ax_3 = fg.add_subplot(gs[1:, 0])
#fig_ax_3.set_title('gs[1:, 0]')

#fig_ax_4 = fg.add_subplot(gs[1:, 1])
#fig_ax_4.set_title('gs[1:, 1]')
#fig_ax_5 = fg.add_subplot(gs[1, 2:])
#fig_ax_5.set_title('gs[1, 2:]')

#fig_ax_6 = fg.add_subplot(gs[2:4, 2])
#fig_ax_6.set_title('gs[2:4, 2]')

#fig_ax_7 = fg.add_subplot(gs[2:4, 3:])
#fig_ax_7.set_title('gs[2:4, 3:]')

#fig_ax_8 = fg.add_subplot(gs[4, 3:])
#fig_ax_8.set_title('gs[4, 3:]')


#3d график
x = np.linspace(-np.pi, np.pi, 50)
y = x
z = np.cos(x)
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot(x, y, z, label='parametric curve')

