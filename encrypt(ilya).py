# encrypt.py
import os
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def encrypt_password_and_save(password, key, file_path):
    try:
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
        
        # Prepend IV to the ciphertext
        encrypted_data = iv + encrypted_password
        
        # Write encrypted data to the file
        with open(file_path, "wb") as key_file:
            key_file.write(f"Key: {key.hex()}".encode())

        print("Encryption complete.")
        return True
    except Exception as e:
        print("Encryption error:", e)
        return False

password = "Pleasework"
key = os.urandom(32)
file_path = "encryption_info.txt"
success = encrypt_password_and_save(password.encode(), key, file_path)
if success:
    print("Encryption successful.")
else:
    print("Encryption failed.")
