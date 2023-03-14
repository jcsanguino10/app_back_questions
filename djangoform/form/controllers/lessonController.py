from ..models import Lesson,CourseEn,CourseEs,CoursePt
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from ..static import parameter
from ..functions import lessonFunctions

@api_view(['GET'])
def getUser(request):
    if request.method == 'GET':
        if (all(key in request.GET for key in [parameter.ID])):
            id = request.GET[parameter.ID]
            try:
                lesson = Lesson.objects.get(id=id)
                response = {}
                response['Lesson'] = lessonFunctions.toDict(lesson)
                return Response(response, status=status.HTTP_200_OK)
            except:
                return Response({"error": "Lesson with id {} not found".format(id)}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "Missing parameters"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    return Response({"error": "Wrong Method"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

@api_view(['POST'])
def createLesson(request):
    print('entra')
    if request.method == 'POST':
        if (all(key in request.POST for key in [parameter.LANGUAGE,
                                                parameter.NUMBER,
                                                parameter.CONTENT,
                                                parameter.FK_COURSE])):
            language = request.POST[parameter.LANGUAGE]
            number = int(request.POST[parameter.NUMBER])
            content = request.POST[parameter.CONTENT]
            fk_course = request.POST[parameter.FK_COURSE]
            response = {}
            if language == 'En':
                try:
                    courseEn = CourseEn.objects.get(id=fk_course)
                    lesson = Lesson(language=language,number=number,content=content,courseEn=courseEn)
                    lesson.save()
                    response['Lesson'] = lessonFunctions.toDict(lesson)
                    return Response(response, status=status.HTTP_200_OK)
                except:
                    return Response({"error": "CourseEn with id {} not found".format(fk_course)}, status=status.HTTP_404_NOT_FOUND)
            elif language == 'Es':
                try:
                    courseEs = CourseEs.objects.get(id=fk_course)
                    lesson = Lesson(language=language,number=number,content=content,courseEs=courseEs)
                    lesson.save()
                    response['Lesson'] = lessonFunctions.toDict(lesson)
                    return Response(response, status=status.HTTP_200_OK)
                except:
                    return Response({"error": "CourseEs with id {} not found".format(fk_course)}, status=status.HTTP_404_NOT_FOUND)
            elif language == 'Pt':
                try:
                    coursePt = CoursePt.objects.get(id=fk_course)
                    lesson = Lesson(language=language,number=number,content=content,coursePt=coursePt)
                    lesson.save()
                    response['Lesson'] = lessonFunctions.toDict(lesson)
                    return Response(response, status=status.HTTP_200_OK)
                except:
                    return Response({"error": "CoursePt with id {} not found".format(fk_course)}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({"error": "Wrong Language Introduced"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)  
        else:
            return Response({"error": "Missing parameters"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    return Response({"error": "Wrong Method"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)