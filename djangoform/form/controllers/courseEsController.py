from ..models import CourseEs,Course
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from ..static import parameter
from ..functions import courseEsFunctions

@api_view(['GET'])
def getCourseEs(request):
    if request.method == 'GET':
        if (all(key in request.GET for key in [parameter.ID])):
            id = request.GET[parameter.ID]
            try:
                courseEs = CourseEs.objects.get(id=id)
                response = {}
                response['CourseEs'] = courseEsFunctions.toDict(courseEs)
                return Response(response, status=status.HTTP_200_OK)
            except:
                return Response({"error": "CourseEs with id {} not found".format(id)}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "Missing parameters"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    return Response({"error": "Wrong Method"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

@api_view(['POST'])
def createCourseEs(request):
    if request.method == 'POST':
        if (all(key in request.POST for key in [parameter.NAME,
                                                parameter.FK_COURSE])):
            name = request.POST[parameter.NAME]
            fk_course = request.POST[parameter.FK_COURSE]
            try:
                course = Course.objects.get(id=fk_course)
                courseEs = CourseEs(name=name, course=course)
                courseEs.save()
                response = {}
                response['CourseEs'] = courseEsFunctions.toDict(courseEs)
                return Response(response, status=status.HTTP_201_CREATED)
            except:
                return Response({"error": "Course with id {} not found".format(fk_course)}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "Missing parameters"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    return Response({"error": "Wrong Method"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)