from django.db import models

class School(models.Model):
    name = models.CharField("שם", max_length=10)
    
    class Meta:
        verbose_name = "בית ספר"
        verbose_name_plural = "בתי ספר"
        
        
class Grade(models.Model):
    year = models.DecimalField("שנה", max_digits=4, decimal_places=0)
    school = models.ForeignKey(School, on_delete=models.CASCADE, verbose_name="בית ספר")
    
    class Meta:
        verbose_name = "שכבה"
        verbose_name_plural = "שכבות" 
         
         
class ClassGroup(models.Model):
    number = models.DecimalField("מספר", max_digits=2, decimal_places=0, default=1)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, verbose_name="שכבה")
    teacher = models.ForeignKey('accounts.Teacher', on_delete=models.PROTECT, blank=True, verbose_name="מורה")

    class Meta:
        verbose_name = "כיתה"
        verbose_name_plural = "כיתות" 
