print("Приветствую, смертный! Сегодня будем шифровать твои сообщения!")
shif = input("Мы будем шифровать или расшифровывать? (s/n): ")
language = input("Смертный, введи язык, на котором будет сообщение (r/e): ")
key = int(input("Введи ключ для шифрования/расшифровки(если не знаете пишите 0): "))
text = input("Введи текст, который будем шифровать/расшифровывать: ")
result = []


def is_russian_letter(char):
    return "а" <= char <= "я" or "А" <= char <= "Я"


def is_english_letter(char):
    return "a" <= char <= "z" or "A" <= char <= "Z"


def encrypt(language, key, text):
    for char in text:
        if is_english_letter(char):
            if char.islower():
                result.append(chr((ord(char) - ord("a") + key) % 26 + ord("a")))
            else:
                result.append(chr((ord(char) - ord("A") + key) % 26 + ord("A")))
        elif is_russian_letter(char):
            if char.islower():
                result.append(chr((ord(char) - ord("а") + key) % 32 + ord("а")))
            else:
                result.append(chr((ord(char) - ord("А") + key) % 32 + ord("А")))
        else:
            result.append(char)  # Сохраняем символ как есть
    return result


def decrypt(language, key, text):
    for char in text:
        if is_english_letter(char):
            if char.islower():
                result.append(chr((ord(char) - ord("a") - key) % 26 + ord("a")))
            else:
                result.append(chr((ord(char) - ord("A") - key) % 26 + ord("A")))
        elif is_russian_letter(char):
            if char.islower():
                result.append(chr((ord(char) - ord("а") - key) % 32 + ord("а")))
            else:
                result.append(chr((ord(char) - ord("А") - key) % 32 + ord("А")))
        else:
            result.append(char)  # Сохраняем символ как есть
    return result


if shif == "s":
    print("".join(encrypt(language, key, text)))
else:
    print("".join(decrypt(language, key, text)))
