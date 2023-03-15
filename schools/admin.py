from django.contrib import admin
from django.contrib.auth.models import Group
from nested_admin import NestedTabularInline, NestedModelAdmin
from .models import School, Grade, ClassGroup
from .forms import ClassGroupForm 


class ClassGroupInline(NestedTabularInline):
    model = ClassGroup
    extra = 0
    
class GradeInline(NestedTabularInline):
    model = Grade
    extra = 0
    inlines = [ClassGroupInline]

class SchoolAdmin(NestedModelAdmin):
    inlines = [GradeInline]

class ClassGroupAdmin(admin.ModelAdmin):
    form = ClassGroupForm


admin.site.register(School, SchoolAdmin)
admin.site.register(Grade)
admin.site.register(ClassGroup, ClassGroupAdmin)

admin.site.unregister(Group)