from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def read_encryption_info(file_path):
    try:
        with open(file_path, "rb") as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith(b"Key:"):
                    key_hex = line.split(b":")[1].strip()
                    key = bytes.fromhex(key_hex.decode())
                    return key
    except Exception as e:
        print("Error reading key:", e)
        return None

def decrypt_password_from_file(file_path):
    try:
        # Read the encrypted data from the file
        with open(file_path, "rb") as file:
            encrypted_data = file.read()

        # Read the key from the file
        key = read_encryption_info(file_path)

        if key:
            # Extract the IV from the encrypted data
            iv = encrypted_data[:16]

            # Create a cipher object
            cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
            decryptor = cipher.decryptor()

            # Decrypt the password
            decrypted_data = decryptor.update(encrypted_data[16:]) + decryptor.finalize()

            # Remove padding to retrieve the original password
            unpadder = padding.PKCS7(128).unpadder()
            unpadded_password = unpadder.update(decrypted_data) + unpadder.finalize()

            return unpadded_password.decode()
        else:
            print("Unable to read key.")
            return None
    except Exception as e:
        print("Decryption error:", e)
        return None

# Define the file path
file_path = "encryption_info.txt"

# Decrypt the password from the file
decrypted_password = decrypt_password_from_file(file_path)
if decrypted_password:
    print("Decrypted password:", decrypted_password)
else:
    print("Failed to decrypt password.")
