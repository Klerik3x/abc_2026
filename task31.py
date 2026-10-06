# Инкапсуляция и property
# todo: Класс "Температура"
# Создайте класс Temperature, который хранит температуру в градусах Цельсия.
# Добавьте свойство для получения и установки температуры в Фаренгейтах и Кельвинах.
# Внутренне температура должна храниться только в Цельсиях.

# celsius (get, set) - работа с Цельсиями.
# fahrenheit (get, set) - при установке конвертирует значение в Цельсии.
# kelvin (get, set) - при установке конвертирует значение в Цельсии.

# Пример использования
# t = Temperature(25)
# print(f"{t.celsius}C, {t.fahrenheit}F, {t.kelvin}K")
# t.fahrenheit = 32
# print(f"После установки 32F: {t.celsius}C")

class Temperature:
    def __init__(self, celsius=0):
        # Внутреннее хранение всегда в Цельсиях
        self._celsius = celsius

    # Свойство для работы с Цельсиями
    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._celsius = value

    # Свойство для работы с Фаренгейтами
    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
    # Конвертация из Фаренгейта в Цельсий при установке
        self._celsius = (value - 32) * 5 / 9

    # Свойство для работы с Кельвинами
    @property
    def kelvin(self):
        return self._celsius + 273.15

    @kelvin.setter
    def kelvin(self, value):
    # Конвертация из Кельвинов в Цельсий при установке
        self._celsius = value - 273.15


t = Temperature(25)
print(f"{t.celsius}C, {t.fahrenheit}F, {t.kelvin}K")

t.fahrenheit = 32
print(f"После установки 32F: {t.celsius}C")
