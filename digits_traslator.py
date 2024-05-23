def menu():
    option = int(input("\n 1. Byte to character \n 2. Word to byte \n 3. Byte to ASCII \n Select a number: "))
    if option == 1:
        char = input("Enter a character to convert to byte: ")
        result = character_byte(char)
        print(f"The character '{char}' in byte is: {result}")
    elif option == 2:
        text = input("Enter the text to convert to binary: ")
        result = word_byte(text)
        print(f"The text '{text}' in bytes is: '{result}'")
    elif option == 3:
        byte = input("Enter the byte to convert to ASCII values: ")
        result = byte_ascii(byte)
        print(f"The binary '{byte}' in ASCII representation is: {result}")
    else:
        print("Invalid option selected.")

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

menu()
