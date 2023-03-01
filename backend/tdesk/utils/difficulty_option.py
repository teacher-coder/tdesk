import collections
import random
from enum import Enum
from typing import List

from .word_position import Direction


class Difficulty(str, Enum):
    EASY = "EASY"
    NORMAL = "NORMAL"
    DIFFICULT = "DIFFICULT"


class DifficultyOption:
    def __init__(self, difficulty: Difficulty) -> None:
        self.difficulty = difficulty
        if self.difficulty == Difficulty.EASY:
            self.width = 10
            self.height = 10

        elif self.difficulty == Difficulty.NORMAL:
            self.width = 20
            self.height = 20

        elif self.difficulty == Difficulty.DIFFICULT:
            self.width = 25
            self.height = 25

    def configure(self, words: List[str]):
        self.__adjust_size(words)
        self.__randomize_direction_options()

    def resize_bigger(self):
        self.width = self.height = self.width + 5

    def revise_source_letters(self, words: str, source_letters):
        top_common_letters = self.__get_top_common_letters(words, 5)

        if self.difficulty == Difficulty.EASY:
            return source_letters

        elif self.difficulty == Difficulty.NORMAL:
            return "".join(random.sample(source_letters, 17)) + top_common_letters

        elif self.difficulty == Difficulty.DIFFICULT:
            return "".join(random.sample(source_letters, 10)) + top_common_letters

    def __get_top_common_letters(self, words, common_num: int):
        string = "".join(words)
        return "".join(
            [i[0] for i in collections.Counter(string).most_common(common_num)]
        )

    def __adjust_size(self, words):
        longest_word = sorted(words, key=len, reverse=True)[0]
        try:
            self.__validate_size(longest_word)
        except ValueError:
            self.width = self.height = (len(longest_word) // 5 + 1) * 5

    def __validate_size(self, longest_word):
        if len(longest_word) >= self.width:
            raise ValueError("Width of puzzle can not be smaller than given word")
        elif len(longest_word) >= self.height:
            raise ValueError("Height of puzzle can not be smaller than given word")

    def get_direction_options(self):
        self.__randomize_direction_options()
        if self.difficulty == Difficulty.EASY:
            self.__randomize_directions_until_conditions_met(
                lambda: self.x_direction + self.y_direction == 1
            )
        elif self.difficulty == Difficulty.NORMAL:
            self.__randomize_directions_until_conditions_met(
                random.choice(
                    [
                        lambda: self.x_direction + self.y_direction == 1,
                        lambda: self.x_direction == 1 and self.y_direction != 0,
                    ]
                )
            )

        elif self.difficulty == Difficulty.DIFFICULT:
            self.__randomize_directions_until_conditions_met(
                random.choice(
                    [
                        lambda: self.x_direction == 1,
                        lambda: self.x_direction == -1 or self.x_direction == 1,
                    ]
                )
            )
        return self.x_direction, self.y_direction

    def __randomize_direction_options(self):
        self.x_direction = random.choice(list(Direction))
        self.y_direction = random.choice(list(Direction))
        while self.x_direction == 0 and self.y_direction == 0:
            self.__randomize_direction_options()

    def __randomize_directions_until_conditions_met(self, condition):
        difficulty_configured = False
        if condition():
            difficulty_configured = True
        while not difficulty_configured:
            self.__randomize_direction_options()
            if condition():
                difficulty_configured = True
