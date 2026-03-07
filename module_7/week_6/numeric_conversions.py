'''
Your program must provide and use the following methods. 
Each method signature must be matched and it must behave as described.
Methods should not display anything on the screen!

def hex_char_decode(digit)
Decodes a single hexadecimal digit and returns its decimal value.

def hex_string_decode(hex)
Decodes an entire hexadecimal string and returns its decimal value.

def binary_string_decode(binary)
Decodes a binary string and returns its decimal value.

def binary_to_hex(binary)
Decodes a binary string, re-encodes it as hexadecimal, and returns the hexadecimal string.

Note: It is common to display hexadecimal numbers with "0x" as the prefix 
(e.g., the number FFFFFFFF is represented as 0xFFFFFFFF. 
Your program must be able to convert a hexadecimal string into a number
regardless of whether it is prefixed with "0x."
Additionally, it must handle the binary prefix "0b". 
It is also common for hex numbers to be typed in lowercase 
(e.g., 0xffffffff); your program must handle upper- and lower-case letters.
'''

def hex_char_decode(digit):
    if digit.upper() == "A":
        return 10
    elif digit.upper() == "B":
        return 11
    elif digit.upper() == "C":
        return 12
    elif digit.upper() == "D":
        return 13
    elif digit.upper() == "E":
        return 14
    elif digit.upper() == "F":
        return 15
    else:
        return int(digit)


def hex_string_decode(hex_str):
    # handle optional 0x / 0X prefix safely
    if len(hex_str) >= 2 and hex_str[0] == "0" and (hex_str[1] == "x" or hex_str[1] == "X"):
        hex_str = hex_str[2:]

    total = 0
    power = len(hex_str) - 1
    for ch in hex_str:
        value = hex_char_decode(ch)
        total += value * (16 ** power)
        power -= 1
    return total


def binary_string_decode(binary_str):
    # handle optional 0b / 0B prefix safely
    if len(binary_str) >= 2 and binary_str[0] == "0" and (binary_str[1] == "b" or binary_str[1] == "B"):
        binary_str = binary_str[2:]

    total = 0
    power = len(binary_str) - 1
    for bit in binary_str:
        total += int(bit) * (2 ** power)
        power -= 1
    return total


def binary_to_hex(binary_str):
    # handle optional 0b / 0B prefix safely
    if len(binary_str) >= 2 and binary_str[0] == "0" and (binary_str[1] == "b" or binary_str[1] == "B"):
        binary_str = binary_str[2:]

    # left-pad with zeros until length is multiple of 4
    while len(binary_str) % 4 != 0:
        binary_str = "0" + binary_str

    hex_str = ""
    for i in range(0, len(binary_str), 4):
        nibble = binary_str[i:i + 4]
        val = binary_string_decode(nibble)

        if val >= 10:
            hex_str += chr(65 + (val - 10))
        else:
            hex_str += str(val)

    return hex_str


def main():
    while True:
        print("Decoding Menu")
        print("-------------")
        print("1. Decode hexadecimal")
        print("2. Decode binary")
        print("3. Convert binary to hexadecimal")
        print("4. Quit")
        print()

        option = input("Please enter an option: ")

        if option == "1":
            s = input("Please enter the numeric string to convert: ")
            print(f"Result: {hex_string_decode(s)}")
            print()

        elif option == "2":
            s = input("Please enter the numeric string to convert: ")
            print(f"Result: {binary_string_decode(s)}")
            print()

        elif option == "3":
            s = input("Please enter the numeric string to convert: ")
            print(f"Result: {binary_to_hex(s)}")
            print()

        elif option == "4":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
