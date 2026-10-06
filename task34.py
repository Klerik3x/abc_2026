# Композиция и вычисляемые свойства
# todo: Класс "Заказ"
# Создайте класс Order (Заказ). Внутри он хранит список экземпляров Product (из предыдущей задачи 37).
# Реализуйте свойство total_price, которое вычисляет общую стоимость заказа на основе цен всех товаров
# в списке. Реализуйте методы add_product(product) и remove_product(product) для управления списком.

# Пример использования
# book = Product("Book", 10)
# pen = Product("Pen", 2)
# order = Order()
# order.add_product(book)
# order.add_product(pen)
# print(f"Общая стоимость: {order.total_price}")  # 12

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order:
    def __init__(self):
        # Внутри храним список экземпляров Product
        self._products = []

    def add_product(self, product):
        """Добавляет товар в заказ"""
        self._products.append(product)

    def remove_product(self, product):
        """Удаляет товар из заказа"""
        if product in self._products:
            self._products.remove(product)
        else:
            print(f"Товар '{product.name}' не найден в заказе.")

    @property
    def total_price(self):
        """
        Вычисляемое свойство: возвращает общую стоимость заказа.
        Суммирует цены всех товаров в списке.
        """
        return sum(product.price for product in self._products)


# Пример использования
book = Product("Book", 10)
pen = Product("Pen", 2)

order = Order()
order.add_product(book)
order.add_product(pen)

print(f"Общая стоимость: {order.total_price}")  # 12

# Проверка удаления
order.remove_product(pen)
print(f"Общая стоимость после удаления ручки: {order.total_price}")  # 10
