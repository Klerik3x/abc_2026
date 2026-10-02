# test.py
from helpers.io import log, read_log
from helpers.crypt import caesar, decrypt


def main():
    # 1. Проверяем логгер
    log("Начало работы программы")
    log("Пользователь вошёл в систему")

    print("\n--- Читаем лог ---")
    for line in read_log():
        print(line.strip())

    # 2. Проверяем шифр
    print("\n--- Шифр Цезаря ---")
    original = "Привет, мир!"
    encrypted = caesar(original, 3)
    decrypted = decrypt(encrypted, 3)

    print(f"Оригинал:     {original}")
    print(f"Зашифровано:  {encrypted}")
    print(f"Расшифровано: {decrypted}")


if __name__ == "__main__":
    main()
