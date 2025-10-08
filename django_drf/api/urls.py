from django.urls import path

from . import views

urlpatterns = [
    path('students/',views.studentsView,name='students'),
    path ('students/<int:pk>/',views.studentsDetailView),
    path('employees/',views.Employees.as_view()),
    ]
