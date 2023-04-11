# функциональные функции (функции высшего порядка) - это функции, которые могут принимать в качестве аргументов и/или возвращать другие функции. Функциональные функции не имеют состояния и используются для обработки и трансформации данных, а также для построения более сложных функций из более простых.
#
# Например, функция map() является функциональной функцией, которая принимает другую функцию и применяет ее к каждому элементу входного списка, возвращая новый список, состоящий из результатов применения функции к каждому элементу.
#
# Нефункциональные функции - это функции, которые имеют внутреннее состояние и изменяют его при выполнении. Такие функции обычно модифицируют глобальные переменные или имеют побочные эффекты.
#
# Например, функция append() для списка является нефункциональной функцией, так как она изменяет состояние списка, добавляя новый элемент в конец.


def count_words(text):

    #Функция для подсчета количества слов в тексте.

    words = text.split()
    return len(words)

def save_resume_to_file(text, filename):

    #Функция для сохранения текста в файл.

    with open(filename, 'w') as file:
        file.write(text)

text = "Lorem ipsum dolor sit amet,  consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.Lorem ipsum dolor sit amet,  consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Lorem ipsum dolor sit amet,  consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
filename = "resume.txt"

# Вызываем функцию count_words
word_count = count_words(text)
print("Количество слов в тексте: ", word_count)

# Вызываем функцию save_resume_to_file
save_resume_to_file(text, filename)
print("Резюме сохранено в файл: ", filename)
