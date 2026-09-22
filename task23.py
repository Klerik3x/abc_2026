from flask import Flask

app = Flask(__name__)

# Главная страница
@app.route("/")
def index():
    return "Главная страница"

# О компании
@app.route("/about")
def about():
    return "О компании"

# Контакты
@app.route("/contacts")
def contacts():
    return "Контакты"

# Список постов
@app.route("/posts")
def posts():
    return "Список постов"

if __name__ == "__main__":
    app.run(debug=True)
