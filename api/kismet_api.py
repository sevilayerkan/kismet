import json
import random
import os

class KismetAPI:
    def __init__(self):
        self.json_file_path = os.path.join(os.path.dirname(__file__), '..', 'kismets', 'kismets.json')

    def get_random_fortune(self):
        try:
            with open(self.json_file_path, 'r') as file:
                fortunes = json.load(file)['fortunes']
                return random.choice(fortunes)
        except Exception as e:
            print(f"Error reading fortunes from file: {e}")
            return 'Unable to retrieve fortune at the moment.'
