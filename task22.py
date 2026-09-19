f = open("text.txt", "w+t")
f.write("Hello\n")

f.seek(0)             # 1. Возвращаем курсор в самое начало файла
content = f.read()    # 2. Читаем всё содержимое файла в переменную
print(content)        # 3. Выводим прочитанное на экран

f.close()
