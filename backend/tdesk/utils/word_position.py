from enum import IntEnum
from random import randint
from typing import List, Tuple


class Direction(IntEnum):
    FORWARD = 1
    STEADY = 0
    BACKWARD = -1
 

class WordPosition:
    def __init__(self, word, width, height):
        self.word_length = len(word)
        self.width = width
        self.height = height

    def __get_positions(
        self, total_length: int, word_length: int, direction: Direction
    ):
        if direction == Direction.FORWARD:
            start_position = randint(0, total_length - word_length)
            positions = [
                i for i in range(start_position, start_position + word_length)
            ]
        elif direction == Direction.STEADY:
            start_position = randint(0, total_length - 1)
            positions = [start_position for _ in range(word_length)]
        elif direction == Direction.BACKWARD:
            start_position = randint(word_length, total_length - 1)
            positions = [
                i for i in range(start_position, start_position - word_length, -1)
            ]
        return positions

    def get_word_positions(
        self, x_direction: Direction, y_direction: Direction
    ) -> List[Tuple[int, int]]:
        word_positions = list( 
            zip(
                self.__get_positions(self.width, self.word_length, x_direction),
                self.__get_positions(self.height, self.word_length, y_direction),
            )
        )
        return word_positions
