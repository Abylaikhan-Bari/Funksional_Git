
def rotate_matrix(matrix):
    # используем функцию zip() для транспонирования матрицы
    transposed = list(zip(*matrix))
    # используем функцию reversed() для разворота каждой строки
    rotated = [list(reversed(row)) for row in transposed]
    return rotated


m = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

rotated_m = rotate_matrix(m)
print(rotated_m)  # [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
