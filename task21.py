# Данные для подстановки
config_values = {
    'app_name': 'NextGen',
    'version': '1.0.0',
    'debug': True,
    'db_host': 'localhost',
    'db_port': 5432,
    'db_name': 'my_database',
    'db_user': 'admin',
    'db_password': 'secret123',
    'api_key': 'ak_123456789',
    'api_secret': 'sk_987654321',
    'base_url': 'https://api.example.com',
    'log_file': '/var/log/app.log',
    'data_dir': '/opt/app/data',
    'temp_dir': '/tmp/app',
    'max_workers': 10,
    'timeout': 30,
    'retry_attempts': 3
}

# 1. Открываем файл, откуда будем брать текст
file_in = open(r'C:\Users\User\PycharmProjects\WelcomeScreen\config_default.txt', 'r', encoding='utf-8')

# 2. Открываем файл, куда будем записывать результат (пишем)
file_out = open(r'C:\Users\User\PycharmProjects\WelcomeScreen\config.txt', 'w', encoding='utf-8')

# 3. Читаем исходный файл построчно
for line in file_in:

    # Проверяем: есть ли в строке знак вопроса?
    if '?' in line:

        # Разрезаем строку по знаку равно на две части
        parts = line.split('=')

        # Берем левую часть (название параметра) и убираем лишние пробелы
        key = parts[0].strip()

        # Смотрим, есть ли такое слово в нашем словаре
        if key in config_values:
            # Если есть - берем значение и превращаем его в текст
            value = str(config_values[key])

            # Собираем строку заново
            new_line = parts[0] + '= ' + value + '\n'

            # Записываем новую строку в выходной файл
            file_out.write(new_line)
        else:
            # Если слова нет в словаре, записываем строку без изменений
            file_out.write(line)
    else:
        # Если знака вопроса нет, просто записываем строку
        file_out.write(line)

# 4. Обязательно закрываем оба файла
file_in.close()
file_out.close()

print("Готово!")
