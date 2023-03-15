from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Student, Teacher

@login_required
def main(request):
    try:
        Student.objects.get(id=request.user.id)
        return redirect('my-journey')
    except Student.DoesNotExist:
        try:
            Teacher.objects.get(id=request.user.id)
            return redirect('student-journeys')
        except Teacher.DoesNotExist:
            return redirect('admin:index')