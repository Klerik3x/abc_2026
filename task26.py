def load_matrix(filename):
    # 1. Читаем файл
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # 2. Превращаем строки в список списков чисел
    matrix = [[int(x) for x in line.split()] for line in lines if line.strip()]

    # 3. Проверяем, что все строки одинаковой длины
    lengths = [len(row) for row in matrix]

    if len(set(lengths)) == 1:
        return matrix
    else:
        return False


# Проверка
result = load_matrix("matrix.txt")
print(result)
