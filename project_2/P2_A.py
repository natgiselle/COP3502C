# Project 2 Part A: RLE with Images
# Natalie Ortiz
# COP3502C
# Professor Aggarwal

import console_gfx

# console_gfx.display_image(console_gfx.test_rainbow)

def display_menu():
    print("RLE Menu")
    print("--------")
    print("0. Exit") # use
    print("1. Load File") # use
    print("2. Load Test Image") # use
    print("3. Read RLE String")
    print("4. Read RLE Hex String")
    print("5. Read Data Hex String")
    print("6. Display Image")
    print("7. Display RLE String")
    print("8. Display Hex RLE Data")
    print("9. Display Hex Flat Data")


def main():
    print("Welcome to the RLE image encoder!")
    print()
    print("Displaying Spectrum Image:")
    console_gfx.display_image(console_gfx.test_rainbow)
    print()
    display_menu()
    while True:
        print()
        option = int(input("Select a Menu Option: "))
        if option == 0:
            break
        elif option == 1: # the user gets the option of enter name of file to load 
            file_name = input("Enter name of file to load: ")
            # load the image
            image_data = console_gfx.load_file(file_name)
            console_gfx.display_image(image_data)
        elif option == 2:
            # load test image and print test image data loaded
            image_data = console_gfx.test_image
            print("Test image data loaded.")
        elif option == 6:
            console_gfx.display_image(image_data)


# if we are running this file run it with this
if __name__ == "__main__":
    main()
    