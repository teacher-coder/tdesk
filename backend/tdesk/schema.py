from ninja import Schema

from .utils.difficulty_option import Difficulty


class WordsearchSchema(Schema):
    difficulty: Difficulty
    is_uppercase: bool
    is_hint_twist: bool
    words: list[str]
