def decode(text):
    parts = text.split()
    result = ""

    for part in parts:
        if part.isdigit():
            num = int(part)
            if num == 0:
                result += " "
            else:
                result += chr(num + 96)
        else:
            result += part  # знаки препинания без пробелов

    return result


print(decode("8 5 12 12 15"))  # hello
print(decode("8 5 12 12 15 , 0 23 15 18 12 4 !"))  # hello, world!
