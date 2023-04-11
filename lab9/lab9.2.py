def create_data():
    """
    Функция, которая создает и возвращает список, кортеж и словарь.
    """
    # Создаем список из названий цветов
    colors = ['red', 'green', 'blue', 'yellow']

    # Создаем кортеж из чисел
    numbers = (1, 2, 3, 4, 5)

    # Создаем словарь из имен и возрастов
    people = {'John': 25, 'Mary': 30, 'Bob': 35}

    # Возвращаем список, кортеж и словарь
    return colors, numbers, people

# Вызываем функцию create_data и получаем список, кортеж и словарь
colors_list, numbers_tuple, people_dict = create_data()

# Выводим содержимое каждой структуры данных
print("Список цветов:", colors_list)
print("Кортеж чисел:", numbers_tuple)
print("Словарь людей:", people_dict)
