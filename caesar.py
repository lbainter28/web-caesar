def alphabet_position(char):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    char_pos = 0
    char = char.lower()
    if char in alphabet:
        char_pos = alphabet.find(char)
        return char_pos

def rotate_character(char, rot):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted_char = ''
    if not char.isalpha():
        encrypted_char += char
    else:
        original_index = alphabet_position(char)
        rotated_index = original_index+rot
        if rotated_index < 26:
            encrypted_char += alphabet[rotated_index]
        else:
            encrypted_char += alphabet[rotated_index % 26]
    if char.isupper():
        return encrypted_char.upper()
    else:
        return encrypted_char

def encrypt(text, rot):
    encrypted_text = ''
    for i in text:
        encrypted_text += rotate_character(i, rot)
    return encrypted_text