
def get_input_string():
    # Функция для получения ввода пользователя
    return input("Введите строку: ")

def get_unique_chars(string):
    # Функция для получения уникальных символов из строки
    return sorted(set(string))

def print_chars(chars):
    # Функция для печати символов
    print("Уникальные символы в алфавитном порядке:")
    for char in chars:
        print(char)

def main():
    # Главная функция программы
    string = get_input_string()
    unique_chars = get_unique_chars(string)
    print_chars(unique_chars)

if __name__ == "__main__":
    main()
