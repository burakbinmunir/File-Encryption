# SHA-512 and HMAC-SHA512 Implementation
This repository contains Python code that implements the SHA-512 hashing algorithm and HMAC-SHA512 for generating hash-based message authentication codes.

# Introduction
This Python codebase provides functionality for hashing messages using the SHA-512 algorithm and generating HMAC-SHA512 digests. The code includes implementations of core cryptographic operations essential for SHA-512 hashing and HMAC (Hash-based Message Authentication Code) generation.

# Features
- ASCII to binary conversion.
- Padding messages to a desired length for SHA-512.
- Core operations such as bitwise operations, rotations, and logical functions used in SHA-512 hashing.
- HMAC-SHA512 functionality for generating hash-based message authentication codes.

# Usage
To use the SHA-512 hashing algorithm:
- Import the necessary functions from the provided code.
- Call the sha512(message, first_block, IV) function, passing the message to be hashed, a boolean first_block indicating whether it's the first block of the message, and the Initialization Vector (IV).

# Example:
### Define the message to be hashed
`message_to_hash` = "Your message here"

### Generate the SHA-512 hash
`hashed_message` = sha512(message_to_hash, True, INITIAL_VECTOR)
print("SHA-512 Hash:", hashed_message)

# For HMAC-SHA512:
# Example:
### Define the key and message
`key` = "Your secret key"
`message_to_authenticate` = "Message to authenticate"

### Generate the HMAC-SHA512 digest
`hmac_digest` = hmac_sha512(key, message_to_authenticate)
print("HMAC-SHA512 Digest:", hmac_digest)

# Code Structure
`ascii_to_binary`: Converts ASCII characters to binary representation.
`pad_message`: Pads the binary message to a desired length.
`convert_to_hex`: Converts binary messages to hexadecimal.
And various functions for implementing the SHA-512 hashing algorithm.
