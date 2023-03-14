from ..models import Lesson,Form,User
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from ..static import parameter
from ..functions import formFunctions

@api_view(['GET'])
def getCourseEn(request):
    if request.method == 'GET':
        if (all(key in request.GET for key in [parameter.ID])):
            id = request.GET[parameter.ID]
            try:
                form = Form.objects.get(id=id)
                response = {}
                response['from'] = formFunctions.toDict(form)
                return Response(response, status=status.HTTP_200_OK)
            except:
                return Response({"error": "Form with id {} not found".format(id)}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "Missing parameters"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    return Response({"error": "Wrong Method"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

@api_view(['POST'])
def createForm(request):
    if request.method == 'POST':
        if (all(key in request.POST for key in [parameter.LANGUAGE_1,
                                                parameter.LANGUAGE_2,
                                                parameter.ANSWER_1,
                                                parameter.ANSWER_2,
                                                parameter.ANSWER_3,
                                                parameter.ANSWER_4,
                                                parameter.ANSWER_5,
                                                parameter.FK_USER,
                                                parameter.FK_LESSON_1,
                                                parameter.FK_LESSON_2])):
            language_1 = request.POST[parameter.LANGUAGE_1]
            language_2 = request.POST[parameter.LANGUAGE_2]
            answer_1 = int(request.POST[parameter.ANSWER_1])
            answer_2 = int(request.POST[parameter.ANSWER_2])
            answer_3 = int(request.POST[parameter.ANSWER_3])
            answer_4 = int(request.POST[parameter.ANSWER_4])
            answer_5 = int(request.POST[parameter.ANSWER_5])
            fk_user = request.POST[parameter.FK_USER]
            fk_lesson_1 = request.POST[parameter.FK_LESSON_1]
            fk_lesson_2 = request.POST[parameter.FK_LESSON_2]
            try:
                user = User.objects.get(id=fk_user)
                try:
                    lesson_1 = Lesson.objects.get(id=fk_lesson_1)
                    try:
                        lesson_2 = Lesson.objects.get(id=fk_lesson_1)
                        form = Form(language_1=language_1, language_2=language_2, answer_1=answer_1,
                                    answer_2=answer_2, answer_3=answer_3, answer_4=answer_4,
                                    answer_5=answer_5,user=user,lesson_1=lesson_1,lesson_2=lesson_2)
                        form.save()
                        response = {}
                        response['form'] = formFunctions.toDict(form)
                        return Response(response, status=status.HTTP_200_OK)
                    except :
                        return Response({"error": "Lesson 2 with id {} not found".format(fk_lesson_2)}, status=status.HTTP_404_NOT_FOUND)
                except:
                    return Response({"error": "Lesson 1 with id {} not found".format(fk_lesson_1)}, status=status.HTTP_404_NOT_FOUND)
            except:
                return Response({"error": "User with id {} not found".format(fk_user)}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "Missing parameters"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    return Response({"error": "Wrong Method"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)