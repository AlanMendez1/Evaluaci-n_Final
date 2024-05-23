from functions import character_byte
from functions import word_byte
from functions import byte_ascii

def menu():
    option = int(input("Select a number: \n 1. Byte to character \n 2. Word to byte \n 3. Byte to ASCII \n"))
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

menu()
