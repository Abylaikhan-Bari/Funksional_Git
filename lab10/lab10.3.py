def rotate_matrix(matrix):
    transposed = list(zip(*matrix))
    rotated = [list(reversed(row)) for row in transposed]
    return rotated


m = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

rotated_m = rotate_matrix(m)
for row in m:
    for element in row:
        # Используем функцию str.format() для вывода каждого элемента в ячейке таблицы
        # Для красоты добавим знаки табуляции между элементами
        print("{:4d}".format(element), end="\t")
    print()
print("\n")
# Используем двойной цикл for для вывода матрицы в виде таблицы 3x3
for row in rotated_m:
    for element in row:
        # Используем функцию str.format() для вывода каждого элемента в ячейке таблицы
        # Для красоты добавим знаки табуляции между элементами
        print("{:4d}".format(element), end="\t")
    print()  # Переходим на новую строку для вывода следующей строки матрицы
