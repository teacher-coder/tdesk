from django.http import HttpResponse
from ninja import NinjaAPI

from .schema import WordsearchSchema
from .service import make_wordsearch_worksheet

api = NinjaAPI()


@api.post("/wordsearch")
def create_wordsearch(
    request,
    wordsearch: WordsearchSchema,
):
    return HttpResponse(
        make_wordsearch_worksheet(wordsearch),
        headers={
            "Content-Disposition": 'attachment; filename="wordsearch.docx"',
            "Content-Type": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            "Access-Control-Expose-Headers": "Content-Disposition",
        },
    )
