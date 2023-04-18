# Считываем имена из файлов и сохраняем их в списках
with open('GirlNames.txt', 'r') as f:
    girl_names = [line.strip() for line in f]

with open('BoyNames.txt', 'r') as f:
    boy_names = [line.strip() for line in f]

# Запрашиваем у пользователя имя для проверки на популярность
name = input("Введите имя для проверки на популярность: ")

# Проверяем, является ли введенное имя популярным среди девочек
if name in girl_names:
    print(f"{name} является одним из самых популярных имен для девочек в Казахстане.")

# Проверяем, является ли введенное имя популярным среди мальчиков
if name in boy_names:
    print(f"{name} является одним из самых популярных имен для мальчиков в Казахстане.")

# Если имя не найдено в обоих списках, выводим сообщение об ошибке
if name not in girl_names and name not in boy_names:
    print(f"{name} не является популярным именем в Казахстане.")
