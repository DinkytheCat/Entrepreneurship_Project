from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
def read_encryption_info(file_path):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith("Key:"):
                    key_hex = line.split(":")[1].strip()
                    key = bytes.fromhex(key_hex)
                    return key
    except Exception as e:
        print("Error with reading the key:", e)
        return None

def decrypt_password_from_file(file_path):
    try:
        #reads file using rb not r
        with open(file_path, "rb") as file:
            encrypted_data = file.read()

        key = read_encryption_info(file_path)

        if key:
            #gets the same iv
            iv = encrypted_data[:16]

            #create the same cipher and aes
            cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
            decryptor = cipher.decryptor()
            
            decrypted_data = decryptor.update(encrypted_data[16:]) + decryptor.finalize()
            #unpads the data
            unpadder = padding.PKCS7(128).unpadder()
            unpadded_password = unpadder.update(decrypted_data) + unpadder.finalize()

            return unpadded_password.decode()
        else:
            print("cant read the key")
            return None
    except Exception as e:
        print("Decryption error:", e)
        return None
file_path = "encryption_info.txt"
decrypted_password = decrypt_password_from_file(file_path)
if decrypted_password:
    print("Decrypted password:", decrypted_password)
else:
    print("Failed to decrypr password.")
