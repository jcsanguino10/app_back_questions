from ..models import User
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from ..static import parameter
from ..functions import userFunctions

@api_view(['GET'])
def getUser(request):
    if request.method == 'GET':
        if (all(key in request.GET for key in [parameter.ID])):
            id = request.GET[parameter.ID]
            try:
                user = User.objects.get(id=id)
                response = {}
                response['User'] = userFunctions.toDict(user)
                return Response(response, status=status.HTTP_200_OK)
            except:
                return Response({"error": "User with id {} not found".format(id)}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "Missing parameters"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    return Response({"error": "Wrong Method"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

@api_view(['POST'])
def createUser(request):
    if request.method == 'POST':
        if (all(key in request.POST for key in [parameter.LOGIN,
                                                parameter.PASSWORD])):
            login = request.POST[parameter.LOGIN]
            hashcode = hash(request.POST[parameter.PASSWORD])
            user = User(login=login, hashcode = hashcode)
            user.save()
            response = {}
            response['User'] = userFunctions.toDict(user)
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Missing parameters"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    return Response({"error": "Wrong Method"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)