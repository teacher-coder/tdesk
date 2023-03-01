import copy
import random
import re
import string
from enum import Enum
from random import shuffle
from typing import Tuple, List

import hgtk


from .difficulty_option import Difficulty, DifficultyOption
from .word_position import WordPosition


class Language(Enum):
    KOREAN = 1
    ENGLISH = 2


class PuzzleData:
    def __init__(
        self,
        words,
        puzzle_difficulty_option: DifficultyOption,
        is_uppercase: bool = False,
        is_hint_twist: bool = False,
    ):

        self.words = list(filter(None, words))

        self.lang: Language
        if hgtk.checker.is_hangul(words[0]):
            self.lang = Language.KOREAN
        else:
            self.lang = Language.ENGLISH
        if self.lang == Language.KOREAN and is_uppercase == True:
            raise ValueError("There is no uppercase in Korean")

        if is_uppercase:
            self.words = [i.upper() for i in self.words]

        self.is_uppercase = is_uppercase
        self.is_hint_twist = is_hint_twist

        self.set_difficulty_option(puzzle_difficulty_option)

    def set_difficulty_option(self, puzzle_difficulty_option: DifficultyOption):
        puzzle_difficulty_option.configure(self.words)
        self.__difficulty_option = puzzle_difficulty_option
        self.puzzle = [
            [0 for _ in range(puzzle_difficulty_option.width)]
            for _ in range(puzzle_difficulty_option.height)
        ]

    @property
    def width(self):
        return self.__difficulty_option.width

    @property
    def height(self):
        return self.__difficulty_option.height

    def make(self):
        self.__make_heading()
        while self.__make_puzzle() == False:
            self.__difficulty_option.resize_bigger()
            self.__empty_puzzle()
        self.__make_hint()

    def __make_heading(self):
        if self.lang == Language.KOREAN:
            self.heading = "낱말 찾기"
        elif self.lang == Language.ENGLISH:
            self.heading = "Word Search"

    def __make_hint(self):
        self.hint = []
        for word in self.words:
            if self.is_hint_twist:
                if self.lang == Language.ENGLISH:
                    spelling = [i for i in word]
                    shuffle(spelling)
                    word = "".join(spelling)
                elif self.lang == Language.KOREAN:
                    chosung_word = ""
                    for chr in word:
                        chosung = hgtk.letter.decompose(chr)[0]
                        chosung_word += chosung
                    word = chosung_word
            self.hint.append(word)

    def __make_puzzle(self):
        for word in sorted(self.words, key=len, reverse=True):
            entering_word_succeed = False
            try_num = 0
            max_try = 30
            while not entering_word_succeed:
                word_positions = WordPosition(
                    word,
                    self.__difficulty_option.width,
                    self.__difficulty_option.height,
                )
                (
                    x_direction,
                    y_direction,
                ) = self.__difficulty_option.get_direction_options()
                positions = word_positions.get_word_positions(
                    x_direction,
                    y_direction,
                )
                if self.__place_for_word_exists(word, positions):
                    self.__fill_word_in_puzzle(word, positions)
                    entering_word_succeed = True
                try_num += 1
                if try_num > max_try:
                    return False

        self.answer = copy.deepcopy(self.puzzle)
        self.__fill_random_letters()
        # [print(i) for i in self.puzzle]
        return True

    def __fill_word_in_puzzle(self, word: str, word_positions: List[Tuple[int, int]]):
        for letter, x, y in zip(word, *zip(*word_positions)):
            self.puzzle[y][x] = letter

    def __fill_random_letters(self):
        for i in range(self.__difficulty_option.height):
            for j in range(self.__difficulty_option.width):
                fill_alph = self.__get_random_letter()
                if self.puzzle[i][j] == 0:
                    self.puzzle[i][j] = fill_alph

    def __get_random_letter(self):
        letter_to_fill: str
        if self.lang == Language.KOREAN:
            with open("wordsearch/helper/random_words.txt", "r") as f:
                data = f.read()
            regex_f = r"[가-힣]+"
            search_target_f = data
            data = "".join(list(set(re.findall(regex_f, search_target_f))))
            source_letters = data
        elif self.lang == Language.ENGLISH:
            if not self.is_uppercase:
                source_letters = string.ascii_lowercase
            else:
                source_letters = string.ascii_uppercase

        source_letters = self.__difficulty_option.revise_source_letters(
            self.words, source_letters
        )
        letter_to_fill = random.choice(source_letters)
        return letter_to_fill

    def __place_for_word_exists(self, word, word_positions: List[Tuple[int, int]]):
        for x, y, letter in zip(*zip(*word_positions), word):
            if not (0 == self.puzzle[y][x] or letter == self.puzzle[y][x]):
                return False
        return True

    def __empty_puzzle(self):
        self.puzzle = [
            [0 for _ in range(self.__difficulty_option.width)]
            for _ in range(self.__difficulty_option.height)
        ]


if __name__ == "__main__":
    english_words = [
        "hello",
        "python",
        "anything",
        "else",
        "witch",
        "campaign",
        "creed",
        "law",
        "small",
        "kidney",
        "basin",
        "theory",
        "refer",
        "cow",
        "twin",
        "quality",
        "wording",
        "punch",
        "perfume",
        "hemispher",
        "training",
        "triangle",
        "opera",
        "gravity",
        "feelings",
    ]
    korean_words = ["경찰관", "오늘의음식점", "낱말찾기퍼즐", "한국어", "민주주의", "헌법", "법원"]
