from django.urls import path
from . import views
from .controllers import userController,courseController,courseEnController, courseEsController, coursePtController,lessonController,formController

urlpatterns = [
    path('hello/', views.hello),
    path('users/get', userController.getUser),
    path('users/create', userController.createUser),
    path('courses/get', courseController.getCourse),
    path('courses/create', courseController.createCourse),
    path('courses_en/get', courseEnController.getCourseEn),
    path('courses_en/create', courseEnController.createCourseEn),
    path('courses_es/get', courseEsController.getCourseEs),
    path('courses_es/create', courseEsController.createCourseEs),
    path('courses_pt/get', coursePtController.getCoursePt),
    path('courses_pt/create', coursePtController.createCoursePt),
    path('lessons/get', lessonController.getUser),
    path('lessons/create', lessonController.createLesson),
    path('forms/get', formController.getCourseEn),
    path('forms/create', formController.createForm),
    path('login/', views.login),
]