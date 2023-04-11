# def compose_functions(f, g):
#     def h(x):
#         return f(g(x))
#     return h
#
# # пример использования
# def square(x):
#     return x * x
#
# def add_one(x):
#     return x + 1
#
# h = compose_functions(square, add_one)
# print(h(2)) # 9 (квадрат числа 2 + 1 = 5)

def compose_functions(f, g):
    def h(x):
        return f(g(x))
    return h

# Пример использования
def square(x):
    return x**2

def add_one(x):
    return x + 1

composed = compose_functions(square, add_one)
result = composed(3)  # Ожидаемый результат: 16
print(result)
