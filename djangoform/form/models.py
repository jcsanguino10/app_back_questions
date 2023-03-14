from django.db import models

class User(models.Model):
    login = models.CharField(max_length=200)
    hashcode = models.TextField()
    
class Course(models.Model):
    name = models.CharField(max_length=200)
    
class CourseEs(models.Model):
    name = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class CourseEn(models.Model):
    name = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
class CoursePt(models.Model):
    name = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Lesson(models.Model):
    language = models.CharField(max_length=200)
    number = models.IntegerField()
    content = models.TextField()
    courseEs = models.ForeignKey(CourseEs,default=None, null=True ,on_delete=models.CASCADE, related_name='lessons_es')
    courseEn = models.ForeignKey(CourseEn,default=None, null=True ,on_delete=models.CASCADE, related_name='lessons_en')
    coursePt = models.ForeignKey(CoursePt,default=None, null=True ,on_delete=models.CASCADE, related_name='lessons_pt')

class Form(models.Model):
    language_1 = models.CharField(max_length=200)
    language_2 = models.CharField(max_length=200)
    answer_1 = models.IntegerField()
    answer_2 = models.IntegerField()
    answer_3 = models.IntegerField()
    answer_4 = models.IntegerField()
    answer_5 = models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    lesson_1 = models.ForeignKey(Lesson,on_delete=models.CASCADE,default=None, null=True, related_name='form_lesson_1')
    lesson_2 = models.ForeignKey(Lesson,on_delete=models.CASCADE,default=None, null=True, related_name='form_lesson_2')
