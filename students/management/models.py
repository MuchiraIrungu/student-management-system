from django.db import models


# Create your models here.
class Student(models.Model):
    student_number = models.PositiveIntegerField()
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    marks = models.FloatField(max_length=40)
    grade = models.CharField(max_length=5)

    def __str__(self):
        return('Student: {self.first_name} {self.last_name}')


