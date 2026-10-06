# Инкапсуляция и property
# todo: Класс "Товар" (Защита от отрицательной цены)
# Создайте класс Product. У него есть свойства name (простая строка) и price.
# При установке цены проверяйте, что она не отрицательная.
# Если пытаются установить отрицательную цену, устанавливайте 0.


# Пример использования
# product = Product("Book", 10)
# print(product.price)  # 10
# product.price = -5
# print(product.price)  # 0

class Product:
    def __init__(self, name, price):
        # Используем сеттеры для первичной установки, чтобы сработала валидация
        self.name = name
        self.price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # Простая установка строки
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        # Проверяем, что цена не отрицательная
        if value < 0:
        # Если пытаются установить отрицательную цену, устанавливаем 0
            self._price = 0
        else:
            self._price = value


# Пример использования
product = Product("Book", 10)
print(product.price) # 10

product.price = -5
print(product.price) # 0
