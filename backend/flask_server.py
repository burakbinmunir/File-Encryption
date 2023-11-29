from flask import Flask, request, jsonify
from flask_cors import CORS 
from aes_enc import encrypt_file, decrypt_file
from sha512_hmac import hmac_sha512


app = Flask(__name__)
CORS(app)
@app.route('/encrypt', methods=['POST'])
def aes_encryption():
    data = request.json 
    
    key = data.get('key')  
    plain_text = data.get('plain_text')
    block_size = data.get('block_size')
    
    if len(key)*8 < block_size:
        while len(key)*8 < block_size:
            key += 'x'
    
    print("from client: " , key, plain_text, block_size)
    
    if not (key and plain_text and block_size):
        return jsonify({'error': 'Missing key, plain_text, or block_size in request'}), 400
    
    encrypted_data = encrypt_file(plain_text, key, block_size)
    print("encrypted data: ", encrypted_data)
    return jsonify({'encrypted_data': encrypted_data})

@app.route('/decrypt', methods=['POST'])
def aes_decryption():
    data = request.json 
    
    key = data.get('key')  
    encrypted_data = data.get('encrypted_data')
    block_size = data.get('block_size')
    
    if len(key)*8 < block_size:
            while len(key)*8 < block_size:
                key += 'x'
    print("from client: " , key, encrypted_data, block_size)
    
    if not (key and encrypted_data and block_size):
        return jsonify({'error': 'Missing key, encrypted_data, or block_size in request'}), 400
    
    decrypted_data = decrypt_file(encrypted_data, key, block_size)
    
    print("decrypted data: ", decrypted_data)
    return jsonify({'decrypted_data': decrypted_data})


@app.route('/hmac', methods=['POST'])
def hash_mac ():
    
    data = request.json
    message = data.get('message')
    key = data.get('key')
    hashed_mac = hmac_sha512(key, message)
    print("hashed mac: ", hashed_mac)
    
    return jsonify({'hashed_mac': hashed_mac})
    
if __name__ == '__main__':
    app.run(host='localhost', port=5000)
