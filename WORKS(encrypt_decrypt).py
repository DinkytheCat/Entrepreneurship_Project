import random
import string
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def encrypt_password(password, key):
    # Generate a random initialization vector (IV)
    iv = os.urandom(16)
    
    # Create a cipher using AES in CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    # Pad the password
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(password) + padder.finalize()
    
    # Encrypt the password
    encrypted_password = encryptor.update(padded_data) + encryptor.finalize()
    print("Encrypted password:", encrypted_password.hex())
    return iv + encrypted_password

def decrypt_password(encrypted_password, key):
    # Extract IV from the encrypted password
    iv = encrypted_password[:16]
    
    # Create a cipher using AES in CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    
    # Decrypt the password
    decrypted_data = decryptor.update(encrypted_password[16:]) + decryptor.finalize()
    
    # Unpad the decrypted data
    unpadder = padding.PKCS7(128).unpadder()
    unpadded_password = unpadder.update(decrypted_data) + unpadder.finalize()
    
    return unpadded_password

chars = string.ascii_letters + string.digits + string.punctuation
password_length = 0
password = ""

while password_length < 7 or password_length > 20:
    length = input("Enter length of password:")
    if length.isdigit():
        password_length = int(length)
        if password_length < 7:
            print("Please make it longer")
        elif password_length > 20:
            print("Please make it shorter")
        else:
            for _ in range(password_length):
                next_character = random.choice(chars)
                password += next_character
    else:
        print("Please enter a valid number")

print("Generated password:", password)

# Generate a random 256-bit (32-byte) key
#password = "Pleasework"
key = os.urandom(32)
with open("encryption_key.txt", "wb") as key_file:
    key_file.write(key)
print(key)
# Encrypt the password
encrypted_password = encrypt_password(password.encode(), key)

# Decrypt the password
decrypted_password = decrypt_password(encrypted_password, key)

print("Decrypted password:", decrypted_password.decode())
