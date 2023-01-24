from django.contrib import admin
from django.contrib.auth.models import Group
from .models import School, Grade, ClassGroup

admin.site.register(School)
admin.site.register(Grade)
admin.site.register(ClassGroup)
admin.site.unregister(Group)