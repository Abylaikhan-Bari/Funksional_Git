# Функциональная функция - это функция,
# которая выполняет определенную операцию и возвращает результат.
# Такая функция не изменяет состояние системы, а зависит только от
# своих входных параметров. Функциональные функции обычно являются
# более предсказуемыми и проще тестируются,
# так как они не имеют побочных эффектов.


def count_words(text):
    """
    Функция для подсчета количества слов в тексте.
    """
    words = text.split()
    return len(words)

def save_resume_to_file(text, filename):
    """
    Функция для сохранения текста в файл.
    """
    with open(filename, 'w') as file:
        file.write(text)

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
filename = "resume.txt"

# Вызываем функцию count_words
word_count = count_words(text)
print("Количество слов в тексте: ", word_count)

# Вызываем функцию save_resume_to_file
save_resume_to_file(text, filename)
print("Резюме сохранено в файл: ", filename)
