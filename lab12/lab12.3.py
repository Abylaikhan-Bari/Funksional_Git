import re
from collections import Counter

# Считываем текст из файла и приводим к нижнему регистру
with open('text.txt', 'r') as f:
    text = f.read().lower()

# Удаляем слова, не несущие смысловой нагрузки
stopwords = ['a', 'an', 'the', 'of', 'and', 'to', 'in', 'that', 'this', 'with']
text = re.sub(r'\b(' + '|'.join(stopwords) + r')\b', '', text)

# Разбиваем текст на слова и подсчитываем количество уникальных слов
words = re.findall(r'\b\w+\b', text)
word_counts = Counter(words)

# Отображаем список наиболее часто встречающихся слов
print("Список наиболее часто встречающихся слов:")
for word, count in word_counts.most_common(10):
    print(f"{word}: {count}")
