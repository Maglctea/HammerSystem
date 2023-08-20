import random
import string


def create_invite_code() -> str:
    # Генерируем случайные символы и цифры
    characters = string.ascii_letters + string.digits + string.punctuation

    # Создаем инвайт-код
    invite_code = ''
    for _ in range(6):
        invite_code += random.choice(characters)

    return invite_code
