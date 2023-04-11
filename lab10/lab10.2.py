
numbers = [2, 4, 6, 8, 10, 11, 12]

if any(num % 2 != 0 for num in numbers):
    print("Список содержит хотя бы одно нечетное число")
else:
    print("Список не содержит нечетных чисел")

if all(num % 2 == 0 for num in numbers):
    print("Все элементы списка четные")
else:
    print("Список содержит нечетные элементы")