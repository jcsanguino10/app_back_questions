from ..models import Lesson
from . import courseEnFunctions, courseEsFunctions,coursePtFunctions

def toDict(lesson:Lesson):
    response = {}
    response['id'] = lesson.id
    response['language'] = lesson.language
    response['number'] = lesson.number
    response['content'] = lesson.content
    if lesson.language == 'En':
        response['courseEn'] = courseEnFunctions.toDict(lesson.courseEn)
        response['courseEs'] = None
        response['coursePt'] = None
    elif lesson.language == 'Es':
        response['courseEn'] = None
        response['courseEs'] = courseEsFunctions.toDict(lesson.courseEs)
        response['coursePt'] = None
    elif lesson.language == 'Pt':
        response['courseEn'] = None
        response['courseEs'] = None
        response['coursePt'] = courseEsFunctions.toDict(lesson.coursePt)
    return response