from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class Teacher(User):
    school = models.ForeignKey('schools.School', on_delete=models.CASCADE, verbose_name="בית ספר")

    class Meta:
        verbose_name = "מורה"
        verbose_name_plural = "מורים"  
        
        
class Student(User):
    class_group = models.ForeignKey('schools.ClassGroup', on_delete=models.CASCADE, verbose_name="כיתה")
        
    class Meta:
        verbose_name = "תלמיד"
        verbose_name_plural = "תלמידים"
