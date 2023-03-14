from ..models import User

def toDict(user:User):
    response = {}
    response['id'] = user.id
    response['login'] = user.login
    response['hashcode'] = user.hashcode
    return response