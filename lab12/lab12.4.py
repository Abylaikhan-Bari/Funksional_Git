import datetime

# Открываем файл с датами и считываем их в список
with open('dates.txt', 'r') as file:
    dates = file.read().splitlines()

# Создаем список кортежей, содержащих дату и количество дней между ней и текущей датой
date_diffs = []
for date in dates:
    date_obj = datetime.datetime.strptime(date, '%Y-%m-%d')
    diff = (datetime.datetime.now() - date_obj).days
    date_diffs.append((date, diff))

# Сортируем список по количеству дней
date_diffs.sort(key=lambda x: x[1])

# Выводим отсортированный список
for date_diff in date_diffs:
    print(date_diff[0])


