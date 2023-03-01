import io

from django.http import HttpResponse
from ninja import NinjaAPI, Schema

from .utils.difficulty_option import Difficulty, DifficultyOption
from .utils.puzzle_data import PuzzleData
from .utils.worksheet import Worksheet

api = NinjaAPI()


class Wordsearch(Schema):
    difficulty: Difficulty
    is_uppercase: bool
    is_hint_twist: bool
    words: list[str]


@api.post("/wordsearch/")
def create_wordsearch(
    request,
    wordsearch: Wordsearch,
):
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
    return HttpResponse(
        bio.getvalue(),
        headers={
            "Content-Disposition": 'attachment; filename="wordsearch.docx"',
            "Content-Type": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            "Access-Control-Expose-Headers": "Content-Disposition",
        },
    )
