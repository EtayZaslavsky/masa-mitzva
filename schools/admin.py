from django.contrib import admin
from django.contrib.auth.models import Group
from nested_admin import NestedTabularInline, NestedModelAdmin
from .models import School, Grade, ClassGroup


class ClassGroupInline(NestedTabularInline):
    model = ClassGroup

class GradeInline(NestedTabularInline):
    model = Grade
    inlines = [ClassGroupInline]

class SchoolAdmin(NestedModelAdmin):
    inlines = [GradeInline]


admin.site.register(School, SchoolAdmin)
admin.site.register(Grade)
admin.site.register(ClassGroup)

admin.site.unregister(Group)