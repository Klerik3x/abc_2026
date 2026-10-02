# Задача 1: максимум из двух
max_of_two = lambda a, b: a if a > b else b
print("Максимум из 5 и 10:", max_of_two(5, 10))


# Задача 2: проверка диапазона
mass = [122, 23, 1425, 23, 768, 4, 67, 998, 4, 6, 867]
checks = list(map(lambda x: 1 <= x <= 130, mass))
print("Проверки диапазона:", checks)


#  Задача 3: нечётные
list_ = [10, 11, 14, 25, 33, 36, 100, 101]
odd = list(filter(lambda val: val % 2 != 0, list_))
print("Нечётные:", odd)


# Задача 4: сортировка по .mp3
files = ['file.txt', 'file2.mp3', 'file.pdf', 'file3.mp3', '.mp3le.doc']
sorted_files = sorted(files, key=lambda x: not x.endswith(".mp3"))
print("Отсортированные:", sorted_files)
