from ..models import Course, CourseEs
from . import courseFunctions

def toDict(courseEn: CourseEs):
    response = {}
    response['id'] = courseEn.id
    response['name'] = courseEn.name
    response['course'] = courseFunctions.toDict(courseEn.course)
    return response