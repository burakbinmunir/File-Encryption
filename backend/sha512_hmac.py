def ascii_to_binary(message):
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    return binary_message

def pad_message(binary_message, desired_length):
    padding_length = desired_length - len(binary_message)
    padded_message = binary_message + '1' + '0' * (padding_length - 1)
    return padded_message


def convert_to_hex(binary_message):
    hex_message = ''
    for i in range(0, len(binary_message), 4):
        hex_digit = hex(int(binary_message[i:i + 4], 2))[2:]
        hex_message += hex_digit
    return hex_message


def Ch(e,f,g):
    e = int(e, 16)
    f = int(f, 16)
    g = int(g, 16)
    result = (e & f) ^ (~e & g)
    
    return hex(result)[2:].zfill(16)

def rotr(n, x, bit_size=64):
    return ((x >> n) | (x << (bit_size - n))) & ((1 << bit_size) - 1)

def Sum0(e):
    e = int(e, 16)
    
    result = rotr(14, e) ^ rotr(18, e) ^ rotr(41, e)
    
    return hex(result)[2:].zfill(16)

def Sum1(a):
    a = int(a, 16)

    result = rotr(28, a) ^ rotr(34, a) ^ rotr(39, a)
    
    return hex(result)[2:].zfill(16)

def Maj(a,b,c):
    a = int(a, 16)
    b = int(b, 16)
    c = int(c, 16)   
    
    result = (a & b) ^ (a & c) ^ (b & c)    
    
    return hex(result)[2:].zfill(16)

def round_0(a, b, c, d, e, f, g, h, k, w,i):
    T1 = hex(int(h, 16) + int(Ch(e,f,g), 16) + int(Sum0(e), 16) + int(w, 16) + int(k, 16))[2:].zfill(16)    
    
    T2 = hex(int(Sum1(a), 16) + int(Maj(a,b,c), 16))[2:].zfill(16)
    
    h = g
    g = f
    f = e
    e = hex(int(d, 16) + int(T1, 16))[2:].zfill(16)
    d = c
    c = b
    b = a
    a = hex(int(T1, 16) + int(T2, 16))[2:].zfill(16)  
    
    return a, b, c, d, e, f, g, h

def add_mod_2_64(hex_a, hex_b):
    # Convert hex strings to integers
    int_a = int(hex_a, 16)
    int_b = int(hex_b, 16)
    
    # Perform addition
    result = (int_a + int_b) % (2**64)
    
    # Convert back to hex
    hex_result = format(result, 'x').zfill(16)  # Ensure 16 characters width
    
    return hex_result

def sha512(message, first_block, IV):
    
    binary_message = ''
    if not first_block:
        binary_message = ascii_to_binary(message)
    else :
        binary_message = message
        
    total_bits = 1024
    desired_length = 896
    
    before_padding = binary_message
    if len(binary_message) < desired_length:
        binary_message = pad_message(binary_message, desired_length) # returns 896 bit padded message in binary
    
    hex_message = convert_to_hex(binary_message)
    
    binary_length = format(len(before_padding), '032b')
    hex_length = hex(int(binary_length, 2))[2:]
    
    hex_message_with_length = hex_message + hex_length
    # print("Hex message with length:", hex_message_with_length)  # Print the hex_message_with_length
    
    words = ['0'] * 80  # Initialize words list with zeros

    # produce 80 words 
    i = 0
    a = 0
    while i < 16:
        words[i] = hex_message_with_length[a:a + 16].zfill(16)
        a += 16
        i += 1
    
    i -= 1
    while i < 80:
        s0 = int(words[i - 15], 16)
        s0 = ((s0 >> 1) | (s0 << 63)) ^ ((s0 >> 8) | (s0 << 56)) ^ (s0 >> 7)
        s1 = int(words[i - 2], 16)
        s1 = ((s1 >> 19) | (s1 << 45)) ^ ((s1 >> 61) | (s1 << 3)) ^ (s1 >> 6)
        words[i] = hex((int(words[i - 16], 16) + s0 + int(words[i - 7], 16) + s1) % 2 ** 64)[2:].zfill(16)
        i += 1
        
    
    round_constant = [
        "428A2F98D728AE22", "7137449123EF65CD", "B5C0FBCFEC4D3B2F", "E9B5DBA58189DBBC",
        "3956C25BF348B538", "59F111F1B605D019", "923F82A4AF194F9B", "AB1C5ED5DA6D8118",
        "D807AA98A3030242", "12835B0145706FBE", "243185BE4EE4B28C", "550C7DC3D5FFB4E2",
        "72BE5D74F27B896F", "80DEB1FE3B1696B1", "9BDC06A725C71235", "C19BF174CF692694",
        "E49B69C19EF14AD2", "EFBE4786384F25E3", "0FC19DC68B8CD5B5", "240CA1CC77AC9C65",
        "2DE92C6F592B0275", "4A7484AA6EA6E483", "5CB0A9DCBD41FBD4", "76F988DA831153B5",
        "983E5152EE66DFAB", "A831C66D2DB43210", "B00327C898FB213F", "BF597FC7BEEF0EE4",
        "C6E00BF33DA88FC2", "D5A79147930AA725", "06CA6351E003826F", "142929670A0E6E70",
        "27B70A8546D22FFC", "2E1B21385C26C926", "4D2C6DFC5AC42AED", "53380D139D95B3DF",
        "650A73548BAF63DE", "766A0ABB3C77B2A8", "81C2C92E47EDAEE6", "92722C851482353B",
        "A2BFE8A14CF10364", "A81A664BBC423001", "C24B8B70D0F89791", "C76C51A30654BE30",
        "D192E819D6EF5218", "D69906245565A910", "F40E35855771202A", "106AA07032BBD1B8",
        "19A4C116B8D2D0C8", "1E376C085141AB53", "2748774CDF8EEB99", "34B0BCB5E19B48A8",
        "391C0CB3C5C95A63", "4ED8AA4AE3418ACB", "5B9CCA4F7763E373", "682E6FF3D6B2B8A3",
        "748F82EE5DEFB2FC", "78A5636F43172F60", "84C87814A1F0AB72", "8CC702081A6439EC",
        "90BEFFFA23631E28", "A4506CEBDE82BDE9", "BEF9A3F7B2C67915", "C67178F2E372532B",
        "CA273ECEEA26619C", "D186B8C721C0C207", "EADA7DD6CDE0EB1E", "F57D4F7FEE6ED178",
        "06F067AA72176FBA", "0A637DC5A2C898A6", "113F9804BEF90DAE", "1B710B35131C471B",
        "28DB77F523047D84", "32CAAB7B40C72493", "3C9EBE0A15C9BEBC", "431D67C49C100D4C",
        "4CC5D4BECB3E42B6", "597F299CFC657E2A", "5FCB6FAB3AD6FAEC", "6C44198C4A475817"
    ]    
    
    a = IV[0]
    b = IV[1]
    c = IV[2]
    d = IV[3]
    e = IV[4]
    f = IV[5]
    g = IV[6]
    h = IV[7]
    
    for i in range(0, 80):
        a, b, c, d, e, f, g, h = round_0(a, b, c, d, e, f, g, h, round_constant[i], words[i],i)
    
    result = [a, b, c, d, e, f, g, h]
    
    a3 = []
    for i in range(0, 8):
        a3.append(add_mod_2_64(IV[i], result[i]))
    
    return a3

def get_extended_key(key, desired_length):
    binary_string = ascii_to_binary(key)
    padding = '0' * (desired_length - len(binary_string))
    return padding + binary_string

def xor_binary(binary1, binary2):
    result = ''
    for bit1, bit2 in zip(binary1, binary2):
        result += '1' if bit1 != bit2 else '0'
    return result

def hmac_sha512 ( key, message ):
    
    desired_message_length = 896
    desired_characters = 112
    
    org_message = message
    
    message_arr = []
    
    if len(message)*8 > desired_message_length:
        while len(message)*8 > desired_message_length:
            message_arr.append(message[:desired_characters])
            message = message[desired_characters:]
        message_arr.append(message)
        message = ''
    else:
        message_arr.append(message)
        
    message = org_message
   
    desired_key_length = 1024
    extended_key_binary = get_extended_key(key, desired_key_length)
    
    ipad = '00110110'
    
    ipad_binary = ipad * 128
    s_ipad = xor_binary(extended_key_binary, ipad_binary)
    
    a = '6a09e667f3bcc908'
    b = 'bb67ae8584caa73b'
    c = '3c6ef372fe94f82b'
    d = 'a54ff53a5f1d36f1'
    e = '510e527fade682d1'
    f = '9b05688c2b3e6c1f'
    g = '1f83d9abfb41bd6b'
    h = '5be0cd19137e2179'

    
    IV = [a, b, c, d, e, f, g, h]
  
    
    # computing hash for inner padded key
    inner_hash = sha512(s_ipad, True, IV)
    hash_message = []
    
    i = 0
    while i < len(message_arr):
        if i == 0:
            hash_message = sha512(message_arr[i], False, inner_hash)
        else:
            hash_message = sha512(message_arr[i], False, hash_message)
        i += 1
    hased_message_str = ''
    for i in hash_message:
        hased_message_str += i
        
    
    opad = '01011100'
    opad_binary = opad * 128
    s_opad = xor_binary(extended_key_binary, opad_binary)
    
    outer_hash = sha512(s_opad, True, IV)
    hash_message = sha512(hased_message_str, False, outer_hash)
    
    hased_message_str = ''
    for i in hash_message:
        hased_message_str += i
        
    return hased_message_str

# key = 'izzah'
# message = '20L1302-Shehryar Munir-35201-1085445-5nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn ssssssssssssssssssssssssssssssssssssssssssssssss 22222222222222222222222222222222222222222222222 oooooooooooooooooooooooooooooooooooooooooooooo jskbqkjbdwbkjdbiFBCebdeiubiubeiubfiewbiuefwbadibfibiubciueiubciue   dbqwidbqwiubdqwiubdiqwuubdiuqwbdiuqb  12i2b ib2iu3 $$##E@DSQ#'
# # digest = sha512(message=message)
# # print(digest)
# hmac_digest = hmac_sha512(key=key, message=message)
# print(hmac_digest)

