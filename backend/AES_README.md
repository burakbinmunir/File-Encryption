# AES Encryption and Decryption Implementation
This Python code implements the AES (Advanced Encryption Standard) encryption and decryption algorithm. It allows for encrypting and decrypting text using various block sizes: 128, 192, and 256 bits.

# Introduction
This implementation provides functions to perform AES encryption and decryption. The encrypt function takes plaintext, a plaintext key, and the desired block size as input and generates the encrypted text. Conversely, the decrypt function takes the encrypted text, the original plaintext key, and the block size and decrypts the text back to its original form.

# Prerequisites
- Python 3.x
- NumPy

# How to Use
- Clone the repository to your local machine.
- Make sure you have the necessary prerequisites installed.
- Run the Python script containing the provided AES encryption and decryption functions.
- Use the encrypt function by passing plaintext, a plaintext key, and the desired block size to generate encrypted text.
- Use the decrypt function by providing the encrypted text, the original plaintext key, and the block size to retrieve the decrypted text.

# Example Usage:
# Encrypt text
`plaintext` = "Your secret message"
`key` = "YourSecretKey123"
`block_size` = 128
`encrypted_text` = encrypt(plaintext, key, block_size)
print("Encrypted Text:", encrypted_text)

# Decrypt text
`decrypted_text` = decrypt(encrypted_text, key, block_size)
print("Decrypted Text:", decrypted_text)

# Code Explanation
The code comprises several functions:
`encrypt`: Takes plaintext, a plaintext key, and block size to generate encrypted text using AES.
`decrypt`: Takes encrypted text, the original plaintext key, and block size to decrypt the text.

There are additional functions for AES operations such as byte substitution, matrix transformations, key expansion, and more.
