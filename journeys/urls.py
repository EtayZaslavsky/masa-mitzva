from django.urls import path
from journeys import views

urlpatterns = [
    path('journey/', views.student_journey, name="my-journey"),
    path('journey/exhibit/<int:num>/', views.student_journey, name="exhibit"),
    path('journeys/', views.journeys, name="student-journeys"),
    path('journeys/grade/<int:grade_id>/', views.journeys, name="student-journeys"),
    path('journeys/grade/<int:grade_id>/class/<int:class_group_id>/', views.journeys, name="student-journeys"),
    path('journey/<int:id>/', views.teacher_journey, name="journey-id"),
    path('journey/<int:id>/exhibit/<int:num>/', views.teacher_journey, name="exhibit-id"),    
  ]