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
