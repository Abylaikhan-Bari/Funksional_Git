# Открываем файл для записи
with open('example.txt', 'w') as f:
    f.write('Hello, world!\n')
    f.write('This is an example file.\n')

# Открываем файл для чтения
with open('example.txt', 'r') as f:
    for line in f:
        print(line.strip())

# Открываем файл для добавления данных
with open('example.txt', 'a') as f:
    f.write('This is some additional text.\n')

# Перезаписываем файл
with open('example.txt', 'w') as f:
    f.write('This is a new line of text.\n')

# Читаем файл еще раз
with open('example.txt', 'r') as f:
    for line in f:
        print(line.strip())
