def alphabet_position(letter):
    if letter.isupper():
        return ord(letter) - ord("A")
    else:
        return ord(letter) - ord("a")

def rotate_character(char, rot):
    if char.isalpha():
        if char.isupper():
            return chr(((alphabet_position(char) + rot) % 26) + ord("A"))
        elif char.islower():
            return chr(((alphabet_position(char) + rot) % 26) + ord("a"))
    return char

def encrypt(text, rot):
    encrypted = ''
    for char in text:
        if char == ' ':
            encrypted += ' '
        else:
            encrypted += rotate_character(char, rot)
    return encrypted
