import io

from .schema import WordsearchSchema
from .utils.difficulty_option import DifficultyOption
from .utils.puzzle_data import PuzzleData
from .utils.worksheet import Worksheet


def make_wordsearch_worksheet(wordsearch: WordsearchSchema):
    difficulty_option = DifficultyOption(wordsearch.difficulty)
    puzzle_data = PuzzleData(
        wordsearch.words,
        difficulty_option,
        wordsearch.is_uppercase,
        wordsearch.is_hint_twist,
    )
    puzzle_data.make()
    worksheet = Worksheet(puzzle_data)
    worksheet.write()
    worksheet.write_answer()
    bio = io.BytesIO()

    worksheet.save(bio)
    bio.seek(0)
    return bio.getvalue()
