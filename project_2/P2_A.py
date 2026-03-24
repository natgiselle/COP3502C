# Project 2 Part C: RLE with Images
# Natalie Ortiz
# COP3502C
# Professor Aggarwal

import console_gfx
# console_gfx.display_image(console_gfx.test_rainbow)



'''
1) Translates data (RLE or raw) to a hexadecimal string (without delimiters).
This method can also aid debugging.
Ex: to_hex_string([3,15,6,4]) returns the string '3f64'
'''
def to_hex_string(data):
    hex_chars = "0123456789abcdef"
    hex_str = ''
    for value in data:
        # hex string has each number value in data list as an index of hex_chars string,
        # which then adds the hexadecimal value equivalent for the letters and numbers to hex_str,
        # making it a full string with the proper value attributed
        # ex: value = 13 so hex_chars[13] = 'd'
        hex_str += hex_chars[value]
    return hex_str


'''
2) Returns number of runs of data in an image data set;
double this result for length of encoded (RLE) list.
Runs cannot be longer than 15.
Ex: count_runs([15,15,15,4,4,4,4,4,4]) returns the int 2
'''
def count_runs(flat_data):
    if len(flat_data) == 0:
        return 0
    run_count = 1
    run_length = 1
    for i in range(1, len(flat_data)):
        # if values match and run_length is under 15, it continues the run
        # increments when value changes or when run_length reaches 15
        # ex: flat_data[2] != flat_data[1] so run_count increments to 2
        if flat_data[i] == flat_data[i-1] and run_length < 15:
            run_length += 1
        else:
            run_count += 1
            run_length = 1
    return run_count


'''
3) Returns encoding (in RLE) of the raw data passed in;
used to generate RLE representation of a data.
Runs cannot be longer than 15.
Ex: encode_rle([15,15,15,4,4,4,4,4,4]) returns the list of ints [3,15,6,4]
'''
def encode_rle(flat_data):
    raw_encoding = []
    run_length = 1
    for i in range(1, len(flat_data)):
        if flat_data[i] == flat_data[i-1] and run_length < 15:
            run_length += 1
        else:
            # appends run_length and the value to raw_encoding and then resets the run_length
            # ex: with 13, 13, 13, 5, 4, 5  raw_encoding gets 3 and 13 appended as the first part and so on
            # making it return raw_encoding with [3, 13, 1, 5, 1, 4, 1, 5]
            raw_encoding.append(run_length)
            raw_encoding.append(flat_data[i-1])
            run_length = 1
    # last run is appended to raw_encoding AFTER loop is executed because the last run is NOT added in the LOOP so it must be appended AFTER
    raw_encoding.append(run_length)
    raw_encoding.append(flat_data[-1])
    return raw_encoding


'''
4) Returns decompressed size RLE data;
used to generate flat data from RLE encoding. (Counterpart to #2)
Ex: get_decoded_length([3,15,6,4]) returns the int 9
'''
def get_decoded_length(rle_data):
    decoded_len = 0
    for i in range(0, len(rle_data), 2):
        # steps through rle_data every 2 indexes making it only land on count values
        # and adds each of those values to decoded_len
        # ex: rle_data[0] = 3 and rle_data[2] = 6 so decoded_len is 9
        decoded_len += rle_data[i]
    return decoded_len


'''
5) Returns the decoded data set from RLE encoded data.
This decompresses RLE data for use. (Inverse of #3)
Ex: decode_rle([3,15,6,4]) returns the list of ints [15,15,15,4,4,4,4,4,4]
'''
def decode_rle(rle_data):
    decoded_set = []
    for i in range (0, len(rle_data), 2):
        # steps through rle data every 2 indexes
        # repeats the rle_value rep_count times and adds to decoded_set
        # ex: rep_count = 3 and rle_value = 14 so it adds [14, 14, 14] to decoded_set
        rep_count = rle_data[i]
        rle_value = rle_data[i+1]
        decoded_set += [rle_value] * rep_count
    return decoded_set


'''
6) Translates a string in hexadecimal format into byte data (can be raw or RLE). (Inverse of #1)
Ex: string_to_data('3f64') returns the list of ints [3,15,6,4]
'''
def string_to_data(data_string):
    hex_chars = '0123456789abcdef'
    str_data = []
    for char in data_string:
        # searches each char in hex_chars using .index() string method
        # which searches for the index of the specified char in a string
        # and that position in the string is its integer value
        # ex: index 15 in hex_chars is char 'f' so 15 is appended to str_data
        str_data.append(hex_chars.index(char.lower()))
    return str_data

'''
7) Translates RLE data into a human-readable representation.
For each run, in order, it should display the run length in decimal (1-2 digits);
the run value in hexadecimal (1 digit); and a delimiter, ':', between runs.
(See examples in the standalone menu section.)
Ex: to_rle_string([15,15,6,4]) returns the string '15f:64'
'''
def to_rle_string(rle_data):
    hex_chars = "0123456789abcdef"
    rle_data_str = ""
    for i in range(0, len(rle_data), 2):
        # gets the repetition count as a DECIMAL number and the value as a HEX char
        # puts the values together as pairs separated by a colon (there is NO COLON BEFORE the first run)
        # ex: rle_data[0] = 14 meaning rle_data[i] = 14 therefore '14' + hex_chars[14] = '14e'
        rep_count = str(rle_data[i])
        rle_value = hex_chars[rle_data[i+1]]
        if rle_data_str != "":
            rle_data_str += ':'
        rle_data_str += rep_count + rle_value
    return rle_data_str

'''
8) Translates a string in human-readable RLE format (with delimiters) into RLE byte data. (Inverse of #7)
Ex: string_to_rle('15f:64') returns the list of ints [15,15,6,4]
'''
def string_to_rle(rle_string):
    # splits rle_string by colons and separates the DECIMAL repetition count from the HEX value
    # the last char before the colon is ALWAYS the HEX value and everything before it is the DECIMAL repetition count
    # ex: when part = '15f' it would find int('15') which is 15 and hex_chars.index('f') is 15
    hex_chars = "0123456789abcdef"
    rle_data = []
    parts = rle_string.split(':')

    for part in parts:
        rep_count = int(part[:-1])
        rle_value = hex_chars.index(part[-1].lower())
        rle_data.append(rep_count)
        rle_data.append(rle_value)
    return rle_data



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
    print()

    # set None for no data if image is NOT loaded
    image_data = None


    while True:
        display_menu()
        print()
        option = (input("Select a Menu Option: "))
        if len(option) != 1 or option not in "0123456789":
            print("Error! Invalid input.")
            continue

        elif option == '0':
            break


        elif option == '1': # the user gets the option of enter name of file to load 
            file_name = input("Enter name of file to load: ")
            # load the image
            image_data = console_gfx.load_file(file_name)


        elif option == '2':
            # load test image and print test image data loaded
            image_data = console_gfx.test_image
            print("Test image data loaded.")
            print()


        elif option == '3':
            # reads an RLE string and converts it to RLE BYTE data then decodes it into FLAT data
            rle_string = input("Enter an RLE string to be decoded: ")
            rle_data = string_to_rle(rle_string)
            image_data = decode_rle(rle_data)
            print()


        elif option == '4':
            # reads a HEX string holding the RLE data and converts it to BYTE data then decodes it into FLAT data
            hex_string = input("Enter the hex string holding RLE data: ")
            rle_data = string_to_data(hex_string)
            image_data = decode_rle(rle_data)
            print()

        elif option == '5':
            # reads a HEX string holding the FLAT data and converts the string directly to BYTE data
            hex_string = input("Enter the hex string holding flat data: ")
            image_data = string_to_data(hex_string)
            print()


        elif option == '6':
            if image_data is None:
                print("Displaying image...")
                print("(no data)")
            else:
                print("Displaying image...")
                console_gfx.display_image(image_data)
                print()


        elif option == '7':
            if image_data is None:
                print("RLE representation: (no data)")
            else:
                # encodes ALL image data to RLE and converts to a readable string
                rle_data = encode_rle(image_data)
                print(f"RLE representation: {to_rle_string(rle_data)}") 
                print()


        elif option == '8':
            if image_data is None:
                print("RLE hex values: (no data)")
            else:
                # encodes ALL image data and converts to HEX string
                rle_data = encode_rle(image_data)
                print(f"RLE hex values: {to_hex_string(rle_data)}")
                print()

        elif option == '9':
            if image_data is None:
                print("Flat hex values: (no data)")
            else:
                # converts ALL image data directly to a HEX string
                print(f"Flat hex values: {to_hex_string(image_data)}")
                print()



# if we are running this file run it with this
if __name__ == "__main__":
    main()
    