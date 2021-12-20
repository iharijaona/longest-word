# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

import random
import string
import requests


class Game:
    def __init__(self):
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))

    def random_grid(self):
        pass

    def is_valid(self, word):
        if not word:
            return False
        letters = self.grid.copy()  # Consume letters from the grid
        for letter in word:
            if letter not in letters:
                return False
        return Game.__check_dictionary(word)

    @staticmethod
    def __check_dictionary(word):
        response = requests.get(
            f"https://wagon-dictionary.herokuapp.com/{word}")
        json_response = response.json()
        return json_response['found']
