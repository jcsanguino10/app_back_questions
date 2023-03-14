from ..models import Course, CourseEn
from . import courseFunctions

def toDict(courseEn: CourseEn):
    response = {}
    response['id'] = courseEn.id
    response['name'] = courseEn.name
    response['course'] = courseFunctions.toDict(courseEn.course)
    return response