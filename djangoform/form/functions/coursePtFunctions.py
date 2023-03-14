from ..models import Course, CoursePt
from . import courseFunctions

def toDict(coursePt:CoursePt):
    response = {}
    response['id'] = coursePt.id
    response['name'] = coursePt.name
    response['course'] = courseFunctions.toDict(coursePt.course)
    return response