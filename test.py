

def caesar_cipher(text, shift):
    # Русский алфавит
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    result = []

    # Приведение сдвига к диапазону длины алфавита
    shift = shift % len(alphabet)

    for char in text:
        if char.lower() in alphabet:
            # Получение индекса символа в алфавите
            is_upper = char.isupper()
            index = alphabet.index(char.lower())
            # Новая позиция с учетом сдвига
            new_index = (index + shift) % len(alphabet)
            # Добавляем зашифрованный символ
            new_char = alphabet[new_index]
            result.append(new_char.upper() if is_upper else new_char)
        else:
            # Оставляем символы, которые не в алфавите, без изменений
            result.append(char)
    
    return ''.join(result)

# Пример использования:
text = "Кто владеет информацией - тот владеет миром."
shift = 3
encrypted_text = caesar_cipher(text, shift)
print("Зашифрованный текст:", encrypted_text)