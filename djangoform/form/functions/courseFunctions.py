from ..models import Course

def toDict(course:Course):
    response = {}
    response['id'] = course.id
    response['name'] = course.name
    return response

def toDictFull(course:Course):
    return 0