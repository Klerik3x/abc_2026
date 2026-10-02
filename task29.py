alphabet = "abcdefghijklmnopqrstuvwxyz"


def caesar_decrypt(text, shift):
    """Расшифровка шифра Цезаря (английский алфавит)."""
    result = ""
    for char in text:
        if char.lower() in alphabet:
            is_upper = char.isupper()
            i = alphabet.index(char.lower())
            new_char = alphabet[(i - shift) % len(alphabet)]
            if is_upper:
                new_char = new_char.upper()
            result += new_char
        else:
            result += char
    return result


encrypted = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."

print("Перебор всех сдвигов:")
print("=" * 60)

for shift in range(1, 27):
    decrypted = caesar_decrypt(encrypted, shift)
    print(f"Сдвиг {shift:2}: {decrypted}")
