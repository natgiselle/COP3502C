# Project 2 Part B: RLE with Images
# Natalie Ortiz
# COP3502C
# Professor Aggarwal


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
        # if values match in flat_data and run_length is under 15 it keeps counting
        # and if one of the two conditions or both are not true run_count increments by 1
        # ex: flat_data[2] != flat_data[1] run_count increments to 2
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
    # last run is appended to raw_encoding AFTER loop is executed because it CANNOT grab it IN THE LOOP
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
        # repeating the rle_value rep_count times and added to decoded_set
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
        # puts the values together as pairs separated by a colon
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