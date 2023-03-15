from django.shortcuts import render
from accounts.models import Teacher, Student
def home(request):
    if request.user.is_authenticated:
        try:
            Student.objects.get(id=request.user.id)
            user_type = "STUDENT"      
        except Student.DoesNotExist:
            try:
                Teacher.objects.get(id=request.user.id)
                user_type = "TEACHER"      
            except Teacher.DoesNotExist:
                user_type = "MANAGER"
    else:
        user_type = None
    return render(request, 'index.html', {'user_type':user_type})