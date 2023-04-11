from functools import reduce

# Определяем список чисел
numbers = [1, 2, 3, 4, 5]

# Используем функцию map для возведения каждого числа в квадрат
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # [1, 4, 9, 16, 25]

# Используем функцию filter для фильтрации четных чисел
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4]

# Используем функцию reduce для вычисления суммы всех чисел
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)  # 15
