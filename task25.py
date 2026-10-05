import random
import pickle
import os

WORDS = ["питон", "программирование", "алгоритм", "компьютер", "клавиатура"]
SAVE_FILE = "save.pkl"


def new_game():
    """Создаёт новую игру."""
    word = random.choice(WORDS)
    return {
        "word": word,
        "guessed": set(),
        "attempts": 6,
        "score": 0
    }


def show_state(state):
    """Показывает состояние игры."""
    word = state["word"]
    guessed = state["guessed"]
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "* "
    print(f"\nСлово: {display}")
    print(f"Очки: {state['score']} | Попытки: {state['attempts']}")


def save_game(state, filename=SAVE_FILE):
    """Сохраняет игру в файл."""
    with open(filename, "wb") as f:
        pickle.dump(state, f)
    print(f"💾 Игра сохранена в {filename}")


def load_game(filename=SAVE_FILE):
    """Загружает игру из файла."""
    if not os.path.exists(filename):
        print("Файл сохранения не найден.")
        return None
    with open(filename, "rb") as f:
        state = pickle.load(f)
    print(f"📂 Игра загружена из {filename}")
    return state


def play(state):
    """Игровой цикл."""
    while True:
        show_state(state)

        # Победа?
        if all(letter in state["guessed"] for letter in state["word"]):
            print("🎉 Победа! Вы угадали слово!")
            return

        # Проигрыш?
        if state["attempts"] <= 0:
            print(f"😢 Попытки кончились. Слово было: {state['word']}")
            return

        # Команды игрока
        command = input("Введите букву (или 'save' для сохранения): ").lower().strip()

        # Сохранение
        if command == "save":
            save_game(state)
            continue

        if len(command) != 1:
            print("Введите ровно одну букву или 'save'.")
            continue

        if command in state["guessed"]:
            print("Вы уже называли эту букву.")
            continue

        state["guessed"].add(command)

        if command in state["word"]:
            state["score"] += 10
            print("✅ Есть такая буква!")
        else:
            state["attempts"] -= 1
            print("❌ Нет такой буквы.")


def main():
    """Главное меню."""
    print("🎡 ПОЛЕ ЧУДЕС 🎡")
    print("1. Новая игра")
    print("2. Загрузить игру")
    print("3. Выход")

    choice = input("Ваш выбор: ").strip()

    if choice == "1":
        state = new_game()
        play(state)
    elif choice == "2":
        state = load_game()
        if state:
            play(state)
        else:
            print("Начинаем новую игру.")
            state = new_game()
            play(state)
    elif choice == "3":
        print("До встречи!")
    else:
        print("Неверный выбор.")


if __name__ == "__main__":
    main()
