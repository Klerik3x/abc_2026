#todo: Выведите все строки данного файла в обратном порядке, допишите их в этот же файл.
# Для этого считайте список всех строк при помощи метода readlines().
#
# Содержимое файла inverted_sort.txt:
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
#
# Результат
# Complex is better than complicated.
# Simple is better than complex.
# Explicit is better than implicit.
# Beautiful is better than ugly.

# 1. Открываем файл для чтения и считываем все строки в список
with open(r'C:\Users\User\PycharmProjects\WelcomeScreen\ inverted_sort.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 2. Переворачиваем список с помощью reversed() и превращаем его обратно в список
# Заодно убираем лишние символы переноса строки с помощью strip()
reversed_lines = [line.strip() for line in reversed(lines)]

# 3. Открываем файл в режиме дозаписи ('a') и записываем перевернутые строки
with open(r'C:\Users\User\PycharmProjects\WelcomeScreen\ inverted_sort.txt', 'a', encoding='utf-8') as file:
    for line in reversed_lines:
        file.write(line + '\n')

print("Файл обновлен.")
