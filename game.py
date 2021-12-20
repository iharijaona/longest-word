# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

import random
import string


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
        return True
