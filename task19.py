algorithm = ["C4.5", "k - means", "Метод опорных векторов",
             "Apriori", "EM", "PageRank", "AdaBoost", "kNN",
             "Наивный байесовский классификатор", "CART"]

file = open('algoritm.csv', 'w', encoding='utf-8')

number = 1

for name in algorithm:
    # Вот здесь добавляем запятую и кавычки
    line = str(number) + ') "' + name + '"\n'

    file.write(line)
    number += 1

file.close()
print("Файл создан - <algoritm.csv>")
