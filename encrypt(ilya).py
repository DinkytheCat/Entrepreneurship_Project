import os
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def encrypt_password_and_save(password, key, file_path):
    try:
        #makes ranodm IV
        iv = os.urandom(16)
        
        #we need a cipher too
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        
        #padding the password
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(password) + padder.finalize()
        
        #main encryption part
        encrypted_password = encryptor.update(padded_data) + encryptor.finalize()
        
        #prepend the iv to the already encrypted passowrd to make it easier to decrypt.
        encrypted_data = iv + encrypted_password
        
        #put the key into the file as a hex
        with open(file_path, "wb") as key_file:
            key_file.write(f"Key: {key.hex()}".encode())

        print("Encryption works.")
        return True
    except Exception as e:
        print("Encryption failed bc:", e)
        return False

password = "Pleasework"
key = os.urandom(32)
file_path = "encryption_info.txt"
success = encrypt_password_and_save(password.encode(), key, file_path)
if success:
    print("Encryption works!!!.")
else:
    print("Encryption failed :(((-")
