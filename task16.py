# # todo: База данных пользователя.
# # Задан массив объектов пользователя
#
# users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
#          {'login': 'Ivan',  'age': 10, 'group': "guest"},
#          {'login': 'Dasha', 'age': 30, 'group': "master"},
#          {'login': 'Fedor', 'age': 13, 'group': "guest"}]
#
# Написать фильтр который будет выводить отсортированные объекты по возрасту(больше введеного)
# ,первой букве логина, и заданной группе.
#
# #Сперва вводится тип сортировки:
# 1. По возрасту
# 2. По первой букве
# 3. По группе
#
# тип сортировки: 1
#
# #Затем сообщение для ввода
# Ввидите критерии поиска: 16
#
# Результат:
# #Пользователь: 'Piter' возраст 23 года , группа  "admin"
# #Пользователь: 'Dasha' возраст 30 лет , группа  "master"

users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
         {'login': 'Ivan', 'age': 10, 'group': "guest"},
         {'login': 'Dasha', 'age': 30, 'group': "master"},
         {'login': 'Fedor', 'age': 13, 'group': "guest"}]

# 1. Тип сортировки
print("Выберите тип сортировки:")
print("1. По возрасту")
print("2. По первой букве логина")
print("3. По группе")

choice = int(input("Тип сортировки: "))

# 2. Критерий
if choice == 1:
    criteria = int(input("Введите возраст: "))
elif choice == 2:
    criteria = input("Введите первую букву логина: ").upper()
elif choice == 3:
    criteria = input("Введите группу: ")
else:
    print("Неверный тип сортировки!")
    criteria = None

# 3. Фильтруем и выводим
if criteria is not None:
    found = False  # флаг: нашли хоть кого-то?

    for user in users:
        # Проверяем условие в зависимости от выбора
        if choice == 1 and user['age'] > criteria:
            match = True
        elif choice == 2 and user['login'][0].upper() == criteria:
            match = True
        elif choice == 3 and user['group'] == criteria:
            match = True
        else:
            match = False

        # Если подходит — выводим
        if match:
            found = True
            print(f"Пользователь: '{user['login']}' возраст {user['age']} года , группа \"{user['group']}\"")

    # Если никого не нашли
    if not found:
        print("Пользователи не найдены.")
