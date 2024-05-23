def character_byte(character):
    number = ord(character)
    binary_str = bin(number)[2:]
    return binary_str

def word_byte(text):
    binary_str = ''
    for char in text:
        number = ord(char)
        binary_char = bin(number)[2:]
        binary_char = binary_char.zfill(8)
        binary_str += binary_char
    return binary_str

def byte_ascii(byte):
    num = int(byte, 2)
    ascii_char = chr(num)
    result = f"{ascii_char}-{num}"
    return result