import os
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def encrypt_password_and_save(password, key, file_path):
    try:
        # Generate a random IV
        iv = os.urandom(16)
        
        # Create a cipher object
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        
        # Pad the password
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(password) + padder.finalize()
        
        # Encrypt the password
        encrypted_password = encryptor.update(padded_data) + encryptor.finalize()
        
        # Prepend the IV to the encrypted password
        encrypted_data = iv + encrypted_password
        
        # Write the key into the file as a hex string
        with open(file_path, "wb") as key_file:
            key_file.write(b"Key: " + key.hex().encode())

        print("Encryption successful.")
        return True
    except Exception as e:
        print("Encryption failed:", e)
        return False

# Define the key and password
key = os.urandom(32)
password = "Pleasework".encode('utf-8')

# Define the file path
file_path = "encryption_info.txt"

# Encrypt the password and save
success = encrypt_password_and_save(password, key, file_path)
if success:
    print("Encryption successful.")
else:
    print("Encryption failed.")
