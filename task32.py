# Инкапсуляция и property
# todo: Класс "Пользователь" (Валидация email)
# Создайте класс User. У него должны быть свойства email и password.
# При установке email проверяйте, что строка содержит символ @ (простая валидация).
# При установке пароля, храните не сам пароль, а его хеш (для простоты можно использовать hash()).
# Сделайте метод check_password(password), который проверяет, соответствует ли хеш переданного
# пароля сохраненному хешу.

# Пример использования
# user = User("test@example.com", "secret")
# print(user.email)  # test@example.com
# # print(user.password) # AttributeError
# print(user.check_password("secret"))  # True
# print(user.check_password("wrong"))   # False

class User:
    def __init__(self, email, password):
        # Используем сеттеры для первичной установки, чтобы сработала валидация
        self.email = email
        self.password = password

    @property
    def email(self):
            return self._email

    @email.setter
    def email(self, value):
            # Простая валидация: проверяем наличие символа '@'
            if '@' not in value:
                raise ValueError("Некорректный email: отсутствует символ '@'")
            self._email = value

    @property
    def password(self):
            return self._password_hash

    @password.setter
    def password(self, value):
            # Храним не сам пароль, а его хеш
            self._password_hash = hash(value)

    def check_password(self, password):
        # Проверяем, соответствует ли хеш переданного пароля сохраненному хешу
        return hash(password) == self._password_hash



user = User("test@example.com", "secret")
print(user.email) # test@example.com

print(user.password)

print(user.check_password("secret")) # True
print(user.check_password("wrong")) # False
