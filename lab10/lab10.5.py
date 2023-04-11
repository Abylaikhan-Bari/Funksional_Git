
def matrix_operation(matrix1, matrix2, operator):
    if operator == "+":
        result = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    elif operator == "-":
        result = [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    elif operator == "*":
        result = [[sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2))) for j in range(len(matrix2[0]))] for i in range(len(matrix1))]
    else:
        return "Invalid operator"
    return result

matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]
operator = "+"
result = matrix_operation(matrix1, matrix2, operator)
print(result)  # Output: [[6, 8], [10, 12]]
