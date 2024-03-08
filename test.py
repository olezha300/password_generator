import random


def generate_password(lenght: int, chars: str) -> str:
    # Генерация пароля
    return "".join(random.sample(chars, lenght))


digits: str = "0123456789"
lowercase_letters: str = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation: str = "#$%&*+-=?@^_"
chars: str = ""

counter_passwords: int = int(input("Количество паролей для генерации: "))
len_of_one_password: int = int(input("Длина одного пароля: "))

while True:
    answer_digits: str = input(f"Включать ли числа из списка {digits}?: ")
    if answer_digits.lower() == "да" or answer_digits.lower() == "yes":
        chars += digits
        break
    elif answer_digits.lower() == "нет" or answer_digits.lower() == "no":
        break
    else:
        print("Введите корректный ответ на вопрос")

while True:
    answer_lowercase_letters: str = input(
        f"Включать ли буквы из списка {lowercase_letters}?: "
    )
    if (
        answer_lowercase_letters.lower() == "да"
        or answer_lowercase_letters.lower() == "yes"
    ):
        chars += lowercase_letters
        break
    elif (
        answer_lowercase_letters.lower() == "нет"
        or answer_lowercase_letters.lower() == "no"
    ):
        break
    else:
        print("Введите корректный ответ на вопрос")

while True:
    answer_uppercase_letters: str = input(
        f"Включать ли буквы из списка {uppercase_letters}?: "
    )
    if (
        answer_uppercase_letters.lower() == "да"
        or answer_uppercase_letters.lower() == "yes"
    ):
        chars += uppercase_letters
        break
    elif (
        answer_uppercase_letters.lower() == "нет"
        or answer_uppercase_letters.lower() == "no"
    ):
        break
    else:
        print("Введите корректный ответ на вопрос")

while True:
    answer_punctuation: str = input(f"Включать ли знаки из списка {punctuation}?: ")
    if answer_punctuation.lower() == "да" or answer_punctuation.lower() == "yes":
        chars += punctuation
        break
    elif answer_punctuation.lower() == "нет" or answer_punctuation.lower() == "no":
        break
    else:
        print("Введите корректный ответ на вопрос")

while True:
    answer_trash: str = input(f"Включать ли символы из списка 'il1Lo0O'?: ")
    if answer_trash.lower() == "да" or answer_trash.lower() == "yes":
        chars += "il1Lo0O"
        break
    elif answer_trash.lower() == "нет" or answer_trash.lower() == "no":
        break
    else:
        print("Введите корректный ответ на вопрос")

for _ in range(counter_passwords):
    print(generate_password(len_of_one_password, chars))
