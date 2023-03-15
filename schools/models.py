from django.db import models
from datetime import datetime

class School(models.Model):
    name = models.CharField("שם", max_length=10, unique=True)
            
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "בית ספר"
        verbose_name_plural = "בתי ספר"

    
class Grade(models.Model):
    year = models.DecimalField("שנה", max_digits=4, decimal_places=0)
    school = models.ForeignKey(School, on_delete=models.CASCADE, verbose_name="בית ספר")
    
    def __str__(self):
        return f'{self.school.name} {self.year}'
    
    def year_name(self):
        current_year = datetime.today().year
        year_diff = current_year - year
        names = {
            1: 'א'
        }
    
    class Meta:
        verbose_name = "שכבה"
        verbose_name_plural = "שכבות" 
        unique_together = [['school', 'year']]

             
class ClassGroup(models.Model):
    number = models.DecimalField("מספר", max_digits=2, decimal_places=0)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, verbose_name="שכבה")
    teacher = models.ForeignKey('accounts.Teacher', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="מורה")

    def __str__(self):
        return f'{self.grade.school.name} {self.grade.year} {self.number}'
    
    class Meta:
        verbose_name = "כיתה"
        verbose_name_plural = "כיתות" 
        unique_together = [['grade', 'number']]
