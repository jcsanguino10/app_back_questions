from ..models import Form
from . import lessonFunctions, userFunctions

def toDict(form:Form):
    response = {}
    response['id'] = form.id
    response['language_1'] = form.language_1
    response['language_2'] = form.language_2
    response['answer_1'] = form.answer_1
    response['answer_2'] = form.answer_2
    response['answer_3'] = form.answer_3
    response['answer_4'] = form.answer_4
    response['answer_5'] = form.answer_5
    response['user'] = userFunctions.toDict(form.user)
    response['lesson_1'] = lessonFunctions.toDict(form.lesson_1)
    response['lesson_2'] = lessonFunctions.toDict(form.lesson_2)
    return response

