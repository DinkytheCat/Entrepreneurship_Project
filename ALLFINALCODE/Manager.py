<<<<<<< patch-9
import json
import os

class PasswordManager:            

    def save(self, data):
        with open(self.file, "w") as file:
            json.dump(data, file, indent=4)

    def __init__(self, file):
        self.file = file
        #test if this works using print statement
        print('object is initialized')

    def read(self):
        with open(self.file, "r") as file:
            data = file.read()

            if os.stat(self.file).st_size == 0:
                return []

            return json.loads(data)
=======
import base64
import hashlib
from Crypto.Cipher import AES

class AES256:
    def __init__(self, key): 
        self.key = hashlib.sha256(key.encode()).digest()
        self.iv = b'\x19=C\x16\x94!m\xddp\xf5\xa7\xc9Z4\xc9P'

    def encrypt(self, plaintext):
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)

        padding_length = 16 - (len(plaintext) % 16)
        plaintext += chr(padding_length) * padding_length

        ciphertext = cipher.encrypt(plaintext.encode())
        return base64.b64encode(self.iv + ciphertext)

    def decrypt(self, ciphertext):
        ciphertext = base64.b64decode(ciphertext)

        iv = ciphertext[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)

        plaintext = cipher.decrypt(ciphertext[16:]).decode()
        padding_length = ord(plaintext[-1])
        return plaintext[:-padding_length]
>>>>>>> main
