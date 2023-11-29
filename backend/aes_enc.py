import cv2
import numpy as np
import base64

def print_matrix(matrix):
    
    for _ in range (len(matrix)):
        for __ in range (len(matrix[_])):
            print (matrix[_][__], end = ' ')
        print ()

def byte_substitution ( matrix):
        
    s_box = [
        ["63", "7C", "77", "7B", "F2", "6B", "6F", "C5", "30", "01", "67", "2B", "FE", "D7", "AB", "76"],
        ["CA", "82", "C9", "7D", "FA", "59", "47", "F0", "AD", "D4", "A2", "AF", "9C", "A4", "72", "C0"],
        ["B7", "FD", "93", "26", "36", "3F", "F7", "CC", "34", "A5", "E5", "F1", "71", "D8", "31", "15"],
        ["04", "C7", "23", "C3", "18", "96", "05", "9A", "07", "12", "80", "E2", "EB", "27", "B2", "75"],
        ["09", "83", "2C", "1A", "1B", "6E", "5A", "A0", "52", "3B", "D6", "B3", "29", "E3", "2F", "84"],
        ["53", "D1", "00", "ED", "20", "FC", "B1", "5B", "6A", "CB", "BE", "39", "4A", "4C", "58", "CF"],
        ["D0", "EF", "AA", "FB", "43", "4D", "33", "85", "45", "F9", "02", "7F", "50", "3C", "9F", "A8"],
        ["51", "A3", "40", "8F", "92", "9D", "38", "F5", "BC", "B6", "DA", "21", "10", "FF", "F3", "D2"],
        ["CD", "0C", "13", "EC", "5F", "97", "44", "17", "C4", "A7", "7E", "3D", "64", "5D", "19", "73"],
        ["60", "81", "4F", "DC", "22", "2A", "90", "88", "46", "EE", "B8", "14", "DE", "5E", "0B", "DB"],
        ["E0", "32", "3A", "0A", "49", "06", "24", "5C", "C2", "D3", "AC", "62", "91", "95", "E4", "79"],
        ["E7", "C8", "37", "6D", "8D", "D5", "4E", "A9", "6C", "56", "F4", "EA", "65", "7A", "AE", "08"],
        ["BA", "78", "25", "2E", "1C", "A6", "B4", "C6", "E8", "DD", "74", "1F", "4B", "BD", "8B", "8A"],
        ["70", "3E", "B5", "66", "48", "03", "F6", "0E", "61", "35", "57", "B9", "86", "C1", "1D", "9E"],
        ["E1", "F8", "98", "11", "69", "D9", "8E", "94", "9B", "1E", "87", "E9", "CE", "55", "28", "DF"],
        ["8C", "A1", "89", "0D", "BF", "E6", "42", "68", "41", "99", "2D", "0F", "B0", "54", "BB", "16"],
    ]
   

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            hex_value = format(matrix[i][j], '02X')  # Convert integer to hex string
            matrix[i][j] = s_box[int(hex_value[0], 16)][int(hex_value[1], 16)]

    
    return matrix

def grt_matrix_frm_plain_text (plain_text, block_size):
    # convert from plain text to binary
    binary_text = ''
    for c in plain_text:
        # print(len(c))
        # print(bin(ord(c))[2:].zfill(8))
        # print(len(bin(ord(c))[2:].zfill(8)))
        binary_text += bin(ord(c))[2:].zfill(8)
        
    
    # print("Binary Text: ", binary_text)
    # print("Binary Text Len: ", len(binary_text))
    # print("Bits in binary text: ", len(binary_text))
    
    # print("Plain Text length: ", len(plain_text))
    # print("Bits in plain text: ", len(plain_text) * 8)      
    # convert from binary to hex
    hex_text = ''
    for i in range(0, len(binary_text), 4):
        hex_text += hex(int(binary_text[i:i+4], 2))[2:]
        
    # print("Hex Text Len: ", len(hex_text))
    # print("Bits in Hex text: ", (len(hex_text)*4))
    # convert from hex to matrix
    rows = 0
    cols = 0
    if block_size == 128:
        rows = 4
        cols = 4
    elif block_size == 192:
        rows = 4
        cols = 6
    elif block_size == 256:
        rows = 4
        cols = 8
    else:
        return None
    
    matrix = [[0 for _ in range(rows)] for _ in range(cols)]
    
    # if len(hex_text) * 4 != block_size:
    #     l = block_size - len(hex_text) * 4
    #     l = l / 4
    #     for _ in range(int(l)):
    #         hex_text += '0'
            
    # a = 0
    # for _ in range(rows):
    #     for __ in range(cols):
    #         matrix[_][__] = hex_text[a] + hex_text[a+1]
    #         a += 2
            
    # print_matrix(matrix)

def generate_matrix_from_plain_text (plain_text, block_size):
    
    if len(plain_text) * 8 != block_size:
        print("Mismatch in length")
        print("Text length: " , len(plain_text))
        print("Bits in text: ", len(plain_text) * 8)
        
        return None
    
    hex_text = ''
    for c in plain_text:
        hex_text += hex(ord(c))[2:].zfill(2)
   
    
    rows = 4
    cols = 0
    if block_size == 128:
        cols = 4
    elif block_size == 192:
        cols = 6
    elif block_size == 256:
        cols = 8
    else:
        return None
    
    matrix =  [[0 for _ in range(cols)] for _ in range(rows)]
   
    a = 0
    for _ in range (rows):
        for __ in range (cols):
            matrix[_][__] = hex_text[a] + hex_text[a + 1]
            a += 2
        

    for _ in range (len(matrix)):
        for __ in range (len(matrix[_])):
            matrix[_][__] = int(matrix[_][__],16)
    return matrix

def metrix_from_decrypted_text(decrypted_text):
    if len(plain_text) * 8 != block_size:
        print("Mismatch in length")
        print("Text length: " , len(plain_text))
        print("Bits in text: ", len(plain_text) * 8)
        
        return None
    
    # hex_text = ''
    # for c in plain_text:
    
    #     hex_text += hex(ord(c))[2:]
   
    
    rows = 0
    cols = 0
    if block_size == 128:
        rows = 4
        cols = 4
    elif block_size == 192:
        rows = 4
        cols = 6
    elif block_size == 256:
        rows = 4
        cols = 8
    else:
        return None
    
    
    matrix =  [[0 for _ in range(rows)] for _ in range(cols)]
    
    
def shift_rows (matrix , block_size):
    c1 = 0
    c2 = 0
    c3 = 0
    
    if block_size == 128:
        c1 = 1
        c2 = 2
        c3 = 3
    elif block_size == 192:
        c1 = 1
        c2 = 2
        c3 = 3
    elif block_size == 256:
        c1 = 1
        c2 = 3
        c3 = 4
    else:
        return None
    
    
    for _ in range (len(matrix)):
        if _ == 1:
            matrix[_] = matrix[_][c1:] + matrix[_][:c1]
        elif _ == 2:
            matrix[_] = matrix[_][c2:] + matrix[_][:c2]
        elif _ == 3:
            matrix[_] = matrix[_][c3:] + matrix[_][:c3]
            
    return matrix

def multiply_by_2(num):
    result = num << 1
    if result & 0x100:
        result ^= 0x11B  # XOR with the irreducible polynomial x^8 + x^4 + x^3 + x + 1
    return result & 0xFF

def multiply_by_3(num):
    return multiply_by_2(num) ^ num

def mix_columns(matrix):
    mix_column_matrix = [
        ['02', '03', '01', '01'],
        ['01', '02', '03', '01'],
        ['01', '01', '02', '03'],
        ['03', '01', '01', '02']
    ]

    rows = len(matrix)
    cols = len(matrix[0])
    result_matrix = [['00' for _ in range(cols)] for _ in range(rows)]

    for col in range(cols):
        for row in range(rows):
            val = 0
            for k in range(rows):
                num1 = int(mix_column_matrix[row][k], 16)
                num2 = int(matrix[k][col], 16)
                if num1 == 1:
                    val ^= num2
                elif num1 == 2:
                    val ^= multiply_by_2(num2)
                elif num1 == 3:
                    val ^= multiply_by_3(num2)
            result_matrix[row][col] = format(val, '02X')

    return result_matrix

def key_byte_substitution(word):
    s_box = [
        0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
        0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
        0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
        0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
        0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
        0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
        0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
        0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
        0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
        0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
        0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
        0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
        0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
        0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
        0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
        0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16,
    ]
    
    return [s_box[b] for b in word]


def rotate(word, num):
    return word[num:] + word[:num]

def key_expansion(key, nk, nb, nr):
    rcon = [
        0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36
    ]
    
    expanded_key = [key[i:i+4] for i in range(0, len(key), 4)]  # Store key bytes in lists
    temp = [0] * 4  # Temporarily hold the bytes
    
    for i in range(nk, nb * (nr + 1)):
        temp = expanded_key[i - 1].copy()
        if i % nk == 0:
            temp = rotate(key_byte_substitution(temp), 1)
            if i // nk - 1 < len(rcon):  # Check if the index is within the range of rcon
                temp[0] ^= rcon[(i // nk) - 1]  # Adjust indexing here
        elif nk > 6 and i % nk == 4:
            temp = key_byte_substitution(temp)
        for j in range(4):
            temp[j] ^= expanded_key[i - nk // 4][j]  # Adjust indexing here
        expanded_key.append(temp.copy())
    
    return expanded_key


def hex_string_to_hex_array(hex_string):
    # Convert hexadecimal string to bytes
    bytes_obj = bytes.fromhex(hex_string)
    
    # Convert bytes to a list of integers
    hex_array = list(bytes_obj)
    
    return hex_array


def add_round_key(matrix, expanded_key, round_num):
    # print("Matrix: :", type(matrix[0][0]))
    # print(type(expanded_key[0][0]))
    # print(type(round_num))
    
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            matrix[row][col] ^= expanded_key[round_num * len(matrix) + col][row]
    return matrix


def encrypt(plain_text, plain_key, block_size):
    matrix = generate_matrix_from_plain_text(plain_text, block_size)
    
    # # matrix = grt_matrix_frm_plain_text(plain_text, block_size)
    
    hex_key = ''
    for c in plain_key:
        hex_key += hex(ord(c))[2:].zfill(2)
    hex_key = hex_string_to_hex_array(hex_key)
    # nk = number of 32-bit words in the key
    # nb = number of columns in the state
    # nr = number of rounds
    nk = 0
    nb = 0
    nr = 0
    if block_size == 128:
        nk = 4  
        nb = 4
        nr = 10
    elif block_size == 192:
        nk = 4
        nb = 6
        nr = 12
    elif block_size == 256:
        nk = 4
        nb = 8
        nr = 14
    else:
        return None
    
    expanded_key = key_expansion(hex_key, nk, nb, nr)
    
    matrix = add_round_key(matrix, expanded_key, 0)
    
    for i in range(1, 10):
        matrix = byte_substitution(matrix)
        matrix = shift_rows(matrix, block_size)
        matrix = mix_columns(matrix)
        
        # converting matrix to int from strings
        for _ in range (len(matrix)):
            for __ in range (len(matrix[_])):
                matrix[_][__] = int(matrix[_][__],16)
        matrix = add_round_key(matrix, expanded_key, i)
    matrix = byte_substitution(matrix)
    matrix = shift_rows(matrix, block_size)
    # converting matrix to int from strings
    for _ in range (len(matrix)):
        for __ in range (len(matrix[_])):
            matrix[_][__] = int(matrix[_][__],16)
    
    
    matrix = add_round_key(matrix, expanded_key, 10)
   
    
    # convert matrix to ascii
    for _ in range (len(matrix)):
        for __ in range (len(matrix[_])):
            # matrix[_][__] = chr(matrix[_][__])
            matrix[_][__] = hex(matrix[_][__])[2:].zfill(2)

   
    # convert to ascii string
    encrypted_text = ''
    for _ in range (len(matrix)):
        for __ in range (len(matrix[_])):
            encrypted_text += matrix[_][__]
    
    return encrypted_text
    

def inverse_shift_rows (matrix , block_size):
    c1 = 0
    c2 = 0
    c3 = 0
    
    if block_size == 128:
        c1 = 1
        c2 = 2
        c3 = 3
    elif block_size == 192:
        c1 = 1
        c2 = 2
        c3 = 3
    elif block_size == 256:
        c1 = 1
        c2 = 3
        c3 = 4
    else:
        return None
    
    
    for _ in range (len(matrix)):
        if _ == 1:
            matrix[_] = matrix[_][-c1:] + matrix[_][:-c1]
        elif _ == 2:
            matrix[_] = matrix[_][-c2:] + matrix[_][:-c2]
        elif _ == 3:
            matrix[_] = matrix[_][-c3:] + matrix[_][:-c3]
            
    return matrix

def multiply_by_9(num):
    return multiply_by_2(multiply_by_2(multiply_by_2(num))) ^ num

def multiply_by_11(num):
    return multiply_by_2(multiply_by_2(multiply_by_2(num))) ^ multiply_by_2(num) ^ num

def multiply_by_13(num):
    return multiply_by_2(multiply_by_2(multiply_by_2(num))) ^ multiply_by_2(multiply_by_2(num)) ^ num

def multiply_by_14(num):
    return multiply_by_2(multiply_by_2(multiply_by_2(num))) ^ multiply_by_2(multiply_by_2(num)) ^ multiply_by_2(num)

def inverse_mix_columns(matrix):
    mix_column_matrix = [
        ['0e', '0b', '0d', '09'],
        ['09', '0e', '0b', '0d'],
        ['0d', '09', '0e', '0b'],
        ['0b', '0d', '09', '0e']
    ]

    rows = len(matrix)
    cols = len(matrix[0])
    result_matrix = [['00' for _ in range(cols)] for _ in range(rows)]

    for col in range(cols):
        for row in range(rows):
            val = 0
            for k in range(rows):
                num1 = int(mix_column_matrix[row][k], 16)
                num2 = matrix[k][col]
                if num1 == 0x09:
                    val ^= multiply_by_9(num2)
                elif num1 == 0x0b:
                    val ^= multiply_by_11(num2)
                elif num1 == 0x0d:
                    val ^= multiply_by_13(num2)
                elif num1 == 0x0e:
                    val ^= multiply_by_14(num2)
            result_matrix[row][col] = format(val, '02X')

    return result_matrix

def inverse_byte_substitution ( matrix):
        
    s_box = [
        ["52", "09", "6A", "D5", "30", "36", "A5", "38", "BF", "40", "A3", "9E", "81", "F3", "D7", "FB"],
        ["7C", "E3", "39", "82", "9B", "2F", "FF", "87", "34", "8E", "43", "44", "C4", "DE", "E9", "CB"],
        ["54", "7B", "94", "32", "A6", "C2", "23", "3D", "EE", "4C", "95", "0B", "42", "FA", "C3", "4E"],
        ["08", "2E", "A1", "66", "28", "D9", "24", "B2", "76", "5B", "A2", "49", "6D", "8B", "D1", "25"],
        ["72", "F8", "F6", "64", "86", "68", "98", "16", "D4", "A4", "5C", "CC", "5D", "65", "B6", "92"],
        ["6C", "70", "48", "50", "FD", "ED", "B9", "DA", "5E", "15", "46", "57", "A7", "8D", "9D", "84"],
        ["90", "D8", "AB", "00", "8C", "BC", "D3", "0A", "F7", "E4", "58", "05", "B8", "B3", "45", "06"],
        ["D0", "2C", "1E", "8F", "CA", "3F", "0F", "02", "C1", "AF", "BD", "03", "01", "13", "8A", "6B"],
        ["3A", "91", "11", "41", "4F", "67", "DC", "EA", "97", "F2", "CF", "CE", "F0", "B4", "E6", "73"],
        ["96", "AC", "74", "22", "E7", "AD", "35", "85", "E2", "F9", "37", "E8", "1C", "75", "DF", "6E"],
        ["47", "F1", "1A", "71", "1D", "29", "C5", "89", "6F", "B7", "62", "0E", "AA", "18", "BE", "1B"],
        ["FC", "56", "3E", "4B", "C6", "D2", "79", "20", "9A", "DB", "C0", "FE", "78", "CD", "5A", "F4"],
        ["1F", "DD", "A8", "33", "88", "07", "C7", "31", "B1", "12", "10", "59", "27", "80", "EC", "5F"],
        ["60", "51", "7F", "A9", "19", "B5", "4A", "0D", "2D", "E5", "7A", "9F", "93", "C9", "9C", "EF"],
        ["A0", "E0", "3B", "4D", "AE", "2A", "F5", "B0", "C8", "EB", "BB", "3C", "83", "53", "99", "61"],
        ["17", "2B", "04", "7E", "BA", "77", "D6", "26", "E1", "69", "14", "63", "55", "21", "0C", "7D"],
    ]
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            hex_value = format(matrix[i][j], '02X')
            matrix[i][j] = s_box[int(hex_value[0], 16)][int(hex_value[1], 16)]
            
    return matrix

def generate_matrix_from_hex_text (hex_text, block_size):
   
    if len(hex_text) * 4 != block_size:
        print("Length of hex_text", len(hex_text) * 4)
        print("Expected length: ", block_size)
        if block_size == 128:
            hex_text = hex_text.zfill(32)
        elif block_size == 192:
            hex_text = hex_text.zfill(48)
        elif block_size == 256:
            hex_text = hex_text.zfill(64)
        else:
            return None
    
    rows = 0
    cols = 0
    if block_size == 128:
        rows = 4
        cols = 4
    elif block_size == 192:
        rows = 4
        cols = 6
    elif block_size == 256:
        rows = 4
        cols = 8
    else:
        return None
    
    
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]
   
    a = 0
    for _ in range (rows):
        for __ in range (cols):
            matrix[_][__] = hex_text[a] + hex_text[a + 1]
            a += 2
    

    for _ in range (len(matrix)):
        for __ in range (len(matrix[_])):
            matrix[_][__] = int(matrix[_][__],16)
    
    return matrix


def decrypt(encrypted_text, plain_key, block_size):
    # decrypted_matrix = generate_matrix_from_plain_text(encrypted_text, block_size)
    
    decrypted_matrix = generate_matrix_from_hex_text(encrypted_text, block_size)
  
    matrix = decrypted_matrix
    
    hex_key = ''
    for c in plain_key:
        hex_key += hex(ord(c))[2:].zfill(2)
    hex_key = hex_string_to_hex_array(hex_key)
    expanded_key = key_expansion(hex_key, nk=4, nb=4, nr=10)
    
    # print("Decrypted Matrix: ", decrypted_matrix)
    matrix = add_round_key(matrix, expanded_key, 10)
    
    matrix = inverse_shift_rows(matrix, block_size)
    matrix = inverse_byte_substitution(matrix)
    
    # # print(type(matrix[0][0]))
    
    for _ in range (len(matrix)):
        for __ in range (len(matrix[_])):
            matrix[_][__] = int(matrix[_][__],16)
            
    # # print(type(matrix[0][0]))
    for i in range(9, 0, -1):   
           
        matrix = add_round_key(matrix, expanded_key, i)
    #     # print(type(matrix[0][0]))
        matrix = inverse_mix_columns(matrix)
    #     # print(type(matrix[0][0]))
        
        for _ in range (len(matrix)):
            for __ in range (len(matrix[_])):
                matrix[_][__] = int(matrix[_][__],16)   
                
        matrix = inverse_shift_rows(matrix, block_size)
        matrix = inverse_byte_substitution(matrix)
        for _ in range (len(matrix)):
            for __ in range (len(matrix[_])):
                matrix[_][__] = int(matrix[_][__],16)
    
    matrix = add_round_key(matrix, expanded_key, 0)
    # print(type(matrix[0][0]))
    # # convert matrix to ascii
    for _ in range (len(matrix)):
        for __ in range (len(matrix[_])):
            matrix[_][__] = hex(matrix[_][__])[2:]
    # print_matrix(matrix)
    # convert to ascii string
    decrypted_text = ''
    for _ in range (len(matrix)):
        for __ in range (len(matrix[_])):
            decrypted_text += chr(int(matrix[_][__],16))
    # convert to ascii string
    
    # decrypted_text = bytes.fromhex(decrypted_text).decode('utf-8') 
    return decrypted_text
    


def encrypt_file (plain_text, key, block_size):
    
    # print("Length of Plain Text: ", len(plain_text))
    # print("Bits in plain text: ", len(plain_text)*8)
    # print("Plain Text: ", plain_text)
    factor = 0
    
    if block_size == 128:
        factor = 16
    elif block_size == 192:
        factor = 24
    elif block_size == 256:
        factor = 32
    else:
        return None
    
    if len(plain_text) % factor != 0:
        l = factor - (len(plain_text) % factor)
        while len(plain_text) % factor != 0:
            plain_text += 'x'
            
    
    

    # print(plain_text)
    # print()
    # print()
    i = 0  
    encrypted_text = ''
    while i < len(plain_text) :
        temp_text = plain_text[i: i+factor]
        # print(temp_text)
        # print(len(temp_text))
        # print(len(temp_text)*8)
        temp_encrypted = encrypt(temp_text, key, block_size)
        encrypted_text += temp_encrypted
        i += factor
        
    
        
    # print("Encrypted Text: ", encrypted_text)
    # print()
    # print()
    return encrypted_text

def decrypt_file (encrypted_text, key, block_size):
   
    factor = 0
    
    if block_size == 128:
        factor = 16 * 2
    elif block_size == 192:
        factor = 24 * 2
    elif block_size == 256:
        factor = 32 * 2
    else:
        return None
    
    i = 0  
    decrypted_text = ''
    while i < len(encrypted_text):
        temp_text = encrypted_text[i:i+factor]
        temp_decrypted = decrypt(temp_text, key, block_size)
        decrypted_text += temp_decrypted
        i += factor
        
    return decrypted_text
    
    
# # Read the image using OpenCV
# image = cv2.imread('test_03.png')  # Replace with the path to your image

# # Check if the image was successfully loaded
# if image is not None:
#     key = 'abcdefghijklmnopqrstuvwx01234567'
#     block_size = 256
#     # Convert the image to grayscale if it's a color image
#     if len(image.shape) > 2 and image.shape[2] > 1:
#         image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Get the dimensions of the image
#     height, width = image.shape[:2]

#     # Convert the image to a 2D numpy array
#     image_array = np.array(image)
#     print(image_array.shape)
#     # Display the dimensions of the image and its 2D array representation
#     print(f"Image dimensions: {height} x {width}")
#     print("2D array representation:")
    
    
#     # encrypted_image_array = np.empty_like(image_array, dtype='object')
#     # for i in range(len(image_array)):
#     #     for j in range(len(image_array[i])):
#     #         encrypted_image_array[i][j] = encrypt_file(str(image_array[i][j]), key, block_size)

#     # # Encode the encrypted image array to Base64
#     # encoded_image_array = np.vectorize(lambda x: base64.b64encode(x.encode('utf-8')).decode('utf-8'))(encrypted_image_array)

#     # # Save encoded encrypted image array to a text file
#     # np.savetxt('encoded_encrypted_image.txt', encoded_image_array, fmt='%s')

#     # Load the encoded encrypted image array back from the text file
#     loaded_encrypted_image_array = np.loadtxt('encoded_encrypted_image.txt', dtype='str')

#     # Decode the loaded array from Base64 and decrypt it
#     decoded_loaded_image_array = np.vectorize(lambda x: decrypt_file(base64.b64decode(x).decode('utf-8'), key, block_size))(loaded_encrypted_image_array)

#     # Reshape the decoded loaded array to its original shape
#     decoded_loaded_image_array = decoded_loaded_image_array.reshape(height, width)

#     # Convert the decrypted array to an image (keeping original color format if applicable)
#     decrypted_image = None
#     if len(image.shape) > 2 and image.shape[2] > 1:  # Color image
#         decrypted_image = decoded_loaded_image_array.astype(np.uint8)
#     else:  # Grayscale image
#         decrypted_image = cv2.cvtColor(decoded_loaded_image_array.astype(np.uint8), cv2.COLOR_GRAY2BGR)

#     # Save the decrypted image
#     cv2.imwrite('decrypted_image.png', decrypted_image)
    
# else:
#     print("Failed to load the image. Please check the file path.")
    


    # print("Length of Plain Text: ", len(plain_text))
    # print("Bits in plain text: ", len(plain_text)*8)
    # print("Plain Text: ", plain_text)

    # key = 
    # block_size = 128

    # encrypted_text = encrypt(plain_text, key, block_size)
    # print("Encrypted Text: ", encrypted_text)
    # decrypted_text = decrypt(encrypted_text, key, block_size)
#     # print("Decrypted Text: ", decrypted_text)
    
# plain_text = 'Burak Bin Munir Shehryar Munir iksnbs bkbsk bsbskk '
# key = 'abcdefghijklmnopqrstuvwx01234567'
# block_size = 256
# e = encrypt_file(plain_text, key, block_size)
# print(e)
# d = decrypt_file(e, key, block_size)
# print(d)

# d = decrypt_file(e, key, block_size)
# print(d)
