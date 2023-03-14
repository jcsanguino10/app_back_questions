from ..models import Course
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from ..static import parameter
from ..functions import courseFunctions

@api_view(['GET'])
def getCourse(request):
    if request.method == 'GET':
        if (all(key in request.GET for key in [parameter.ID])):
            id = request.GET[parameter.ID]
            try:
                course = Course.objects.get(id=id)
                response = {}
                response['Course'] = courseFunctions.toDict(course)
                return Response(response, status=status.HTTP_200_OK)
            except:
                return Response({"error": "User with id {} not found".format(id)}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "Missing parameters"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    return Response({"error": "Wrong Method"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

@api_view(['GET'])
def getCourseFull(request):
    if request.method == 'GET':
        if (all(key in request.GET for key in [parameter.ID])):
            id = request.GET[parameter.ID]
            try:
                course =Course.objects.get(id=id)
                response = {}
                response['course'] = courseFunctions.toDictFull(course)
                return response(response, status=status.HTTP_200_OK)
            except:
                return Response({"error": "Course with id {} not found".format(id)}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "Missing parameters"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    return Response({"error": "Wrong Method"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

@api_view(['POST'])
def createCourse(request):
    if request.method == 'POST':
        if (all(key in request.POST for key in [parameter.NAME])):
            name = request.POST[parameter.NAME]
            course = Course(name=name)
            course.save()
            response = {}
            response['Course'] = courseFunctions.toDict(course)
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Missing parameters"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    return Response({"error": "Wrong Method"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)