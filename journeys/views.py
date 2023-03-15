from django.urls import reverse
from django.http import Http404
from django.core.exceptions import PermissionDenied 
from django.shortcuts import render, get_object_or_404
from django.forms import modelform_factory
from .models import Journey, Exhibit0, Exhibit1, Exhibit2, Exhibit3, Exhibit4, Exhibit5, Exhibit6, Exhibit7, Exhibit8, Exhibit9, Exhibit10, Exhibit11, Exhibit12, Exhibit13
from accounts.models import Student, Teacher
from django.contrib.auth.decorators import user_passes_test
from schools.models import ClassGroup

def is_teacher(user):
    try:
        Teacher.objects.get(id=user.id)
        return True
    except:
        return False

def is_student(user):
    try:
        Student.objects.get(id=user.id)
        return True
    except:
        return False

def is_teacher_or_student(user):
    return is_teacher(user) or is_student(user)

def get_exhibit_model(num):      
    exhibits_dict={
        0: Exhibit0,
        1: Exhibit1,
        2: Exhibit2,
        3: Exhibit3,
        4: Exhibit4,
        5: Exhibit5,
        6: Exhibit6,
        7: Exhibit7,
        8: Exhibit8,
        9: Exhibit9,
        10: Exhibit10,
        11: Exhibit11,
        12: Exhibit12,
        13: Exhibit13,
    }
    if num not in exhibits_dict.keys():
        raise Http404("אין תחנה כזו")
    else:
        return exhibits_dict[num]

def exhibit_to_dict(exhibit_instance):
    fields = []
    for field in exhibit_instance._meta.concrete_fields:
        field_name = field.verbose_name
        if field_name not in ['ID', 'exhibit ptr']:
            field = {
                'name': field_name,
                'value': field.value_from_object(exhibit_instance),
                'type': field.get_internal_type()
                } 
            fields.append(field)
    return fields

@user_passes_test(is_teacher, login_url="main", redirect_field_name=None)
def teacher_journey(request, id, num=0):
    teacher = get_object_or_404(Teacher, id=request.user.id)
    try:
        journey = get_object_or_404(Journey, id=id, student__class_group__teacher=teacher)
    except:
        raise Http404("התלמיד לא בכיתה של המורה המחובר")
    if not num:
        num = journey.current_exhibit  
    exhibit_instance = getattr(journey, f'exhibit_{num}')
    return render(request, 'view.html', {'fields_list': exhibit_to_dict(exhibit_instance), 'journey_id':id, 'title': exhibit_instance._meta.verbose_name})  

@user_passes_test(is_student, login_url="home", redirect_field_name=None)
def student_journey(request, num=0):
    journey = get_object_or_404(Journey, student__id=request.user.id)
    if not num:
        num = journey.current_exhibit  
    exhibit_model = get_exhibit_model(num)
    exhibit_form = modelform_factory(exhibit_model, fields=("__all__"))
    exhibit_instance = getattr(journey, f'exhibit_{num}')
    submitted = False
    if request.method == 'POST':
        form = exhibit_form(request.POST, request.FILES, instance=exhibit_instance)
        if form.is_valid():
            exhibit_instance.save()
            setattr(journey, 'current_exhibit', num) 
            journey.save()
            submitted = True
    else:
        form = exhibit_form(instance=exhibit_instance)
    context = {'form': form, 'submitted': submitted,'title': exhibit_instance._meta.verbose_name, 'sub_title': exhibit_instance.label}
    if hasattr(exhibit_instance, 'quote'):
        context['quote'] = getattr(exhibit_instance, 'quote') 
    return render(request, 'form.html', context)  

@user_passes_test(is_teacher, login_url="home", redirect_field_name=None)
def journeys(request, grade_id=0, class_group_id=0):
    teacher = get_object_or_404(Teacher, id=request.user.id)

    if grade_id and class_group_id:
        students = Student.objects.filter(class_group__teacher=teacher, class_group__id=class_group_id)
    elif grade_id:
        students = Student.objects.filter(class_group__teacher=teacher, class_group__grade__id=grade_id)
    else:
        students = Student.objects.filter(class_group__teacher=teacher)

    if students:
        class_groups = ClassGroup.objects.filter(teacher=teacher)
        return render(request, 'students_list.html', {'teacher':teacher, 'class_groups':class_groups, 'students_list':students, 'title':'מסעות תלמידיי'})
    else:
        raise Http404("אין תלמידים למורה")
#
