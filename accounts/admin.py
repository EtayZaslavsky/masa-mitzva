from django.contrib import admin
from .models import Teacher, Student
from schools.models import School, Grade, ClassGroup
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
from import_export.fields import Field
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned, ValidationError
from django.contrib.auth.admin import UserAdmin
                
class ClassGroupForeignKeyWidget(ForeignKeyWidget):
    def clean(self, value, row, **kwargs):
        search_dict = {
            'grade_year':row["שכבה"],
            'school_name':row["בית ספר"],
            'class_number':row["כיתה"] 
        }
        if any(search_dict):
            try:
                school = School.objects.get(name=search_dict['school_name'])
                grade = Grade.objects.get(school=school, year=search_dict['grade_year'])
                class_group = ClassGroup.objects.get(grade=grade, number=search_dict['class_number'])
                return class_group     
            except ObjectDoesNotExist:
                print("object doesn't exist.")          
            except MultipleObjectsReturned:
                print("multiple objects returned.")   
        else:
            ValidationError(_('Invalid value'), code='invalid')    
            
            
class StudentResource(resources.ModelResource):
    id = Field(attribute='id', column_name='מזהה')
    username = Field(attribute='username', column_name='שם משתמש')
    first_name = Field(attribute='first_name', column_name='שם פרטי')
    last_name = Field(attribute='last_name', column_name='שם משפחה')
    school = Field(column_name='בית ספר')
    grade = Field(column_name='שכבה')
    class_group = Field(attribute='class_group', column_name='כיתה', widget=ClassGroupForeignKeyWidget(ClassGroup))

    class Meta:
        model = Student
        fields = ('id', 'username', 'first_name', 'last_name', 'school', 'grade', 'class_group')
        export_order = ('id', 'username', 'first_name', 'last_name', 'school', 'grade', 'class_group')       
        use_natural_foreign_keys = True
                
    def dehydrate_school(self, student):      
        if hasattr(student, 'class_group'): return getattr(student.class_group.grade.school, "name", "לא ידוע")

    def dehydrate_grade(self, student):
        if hasattr(student, 'class_group'): return getattr(student.class_group.grade, "year", "לא ידוע")


class StudentAdmin(ImportExportModelAdmin, UserAdmin):
    fieldsets = ((None, {'fields': ('username', 'password', 'first_name', 'last_name', 'class_group')}),)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'class_group'),
        }),
    )
    resource_classes = [StudentResource]
    
class TeacherAdmin(UserAdmin):
    fieldsets = ((None, {'fields': ('username', 'password', 'first_name', 'last_name', 'school')}),)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'school'),
        }),
    )

admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)