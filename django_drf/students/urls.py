from django.urls import path
from . import views

urlpatterns = [
    path('', views.students),  # ya koi bhi function name jo aapne views.py me banaya ho
]
