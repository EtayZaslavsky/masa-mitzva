from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_TYPE = {
        'STUDENT': 'Student',
        'TEACHER': 'Teacher'
    }


class Teacher(User):
    USER_TYPE = 'TEACHER'
    school = models.ForeignKey('schools.School', on_delete=models.CASCADE, verbose_name="בית ספר")

    def __str__(self):
        return f'{self.school.name} | {self.first_name} {self.last_name}'
    
    class Meta:
        verbose_name = "מורה"
        verbose_name_plural = "מורים"  
        
        
class Student(User):
    USER_TYPE = 'STUDENT'
    class_group = models.ForeignKey('schools.ClassGroup', on_delete=models.CASCADE, verbose_name="כיתה")
        
    class Meta:
        verbose_name = "תלמיד"
        verbose_name_plural = "תלמידים"
