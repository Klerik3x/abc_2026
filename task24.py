# Два алфавита: строчный и заглавный
lower = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
upper = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

# Открываем файл для чтения
with open("message.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()  # читаем все строки в список

# Обрабатываем каждую строку с её номером
for line_number, line in enumerate(lines, start=1):
    shift = line_number  # сдвиг = номер строки (1, 2, 3, ...)
    result = ""  # здесь будем собирать зашифрованную строку

    for char in line:
        if char in lower:
            # строчная буква
            index = lower.index(char)  # её индекс
            new_index = (index - shift) % len(lower)  # сдвиг влево
            result += lower[new_index]
        elif char in upper:
            # заглавная буква
            index = upper.index(char)
            new_index = (index - shift) % len(upper)
            result += upper[new_index]
        else:
            # не буква кириллицы — оставляем как есть
            result += char

#в файле message.txt содержимое следующее
#абв
#про

    # Выводим зашифрованную строку
    print(result)
