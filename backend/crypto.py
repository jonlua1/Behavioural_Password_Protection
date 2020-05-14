# crypto algorithms used
# Scrypt hash
# AES 256 encryption/decryption using pycryptodome library

from base64 import b64encode, b64decode
import hashlib
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

#encrypt plain_text with password
#return encrypted data in bytes
def encrypt(plain_text, password):
    # generate a random salt
    salt = get_random_bytes(AES.block_size)

    # use the Scrypt KDF to get a private key from the password
    private_key = hashlib.scrypt(
        password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)

    # create cipher config
    cipher_config = AES.new(private_key, AES.MODE_GCM)

    # return encrypted data in bytes
    cipher_text, tag = cipher_config.encrypt_and_digest(bytes(plain_text, 'utf-8'))
    data = salt + cipher_config.nonce + cipher_text + tag
    return data

#decrypt ciphertext with password
#return plaintext
def decrypt(data, password):
    salt = data[:16]
    nonce = data[16:32]
    cipher_text = data[32:-16]
    tag = data[-16:]

    # generate the private key from the password and salt
    private_key = hashlib.scrypt(
        password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)

    # create the cipher config
    cipher = AES.new(private_key, AES.MODE_GCM, nonce=nonce)

    # decrypt the cipher text
    decrypted = cipher.decrypt_and_verify(cipher_text, tag)

    return decrypted

#hash given password
#returns data in the form of salt and hashed password
def generate_hash(password):
    # generate a random salt
    salt = get_random_bytes(AES.block_size)

    # use the Scrypt KDF to get a private key from the password
    private_key = hashlib.scrypt(
        password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)

    #salt = data[:16]
    #private_key = data[16:]
    data = salt + private_key

    return data

#to authenticate password
#take the salt and key from the data
#and compare with the derived key generated from the password
#return True if password is valid
#return False if password is invalid
def check_hash(data, password):
    salt = data[:16]
    # use the Scrypt KDF to get a private key from the password
    private_key = hashlib.scrypt(
        password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)
    
    if data[16:] == private_key:
        return True
    else:
        return False

