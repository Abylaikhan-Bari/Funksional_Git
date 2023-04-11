import datetime
import numpy as np

# Вывод текущей даты и времени
print("Текущая дата и время:", datetime.datetime.now())

# Генерация массива случайных чисел
arr = np.random.randint(low=1, high=100, size=10)

# Вывод полученного массива
print("Массив случайных чисел:", arr)

# Вычисление среднего арифметического значения массива
mean = np.mean(arr)
print("Среднее арифметическое:", mean)

# Вычисление медианы массива
median = np.median(arr)
print("Медиана:", median)

# Определение минимального значения массива
min_value = np.amin(arr)
print("Минимальное значение:", min_value)

# Определение максимального значения массива
max_value = np.amax(arr)
print("Максимальное значение:", max_value)
