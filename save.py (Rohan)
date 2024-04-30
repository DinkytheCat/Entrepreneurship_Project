import json
import os

class Saver:
    def _init_(self, file):
        save.file = file

    def save(self, data):
        with open(self.file, "w") as file:
            json.dump(data, file, indent=4)

    def read(self):
        with open(self.file, "r") as file:
            data = file.read()

            if os.stat(self.file).st_size == 0:
                return []

            return json.loads(data)
