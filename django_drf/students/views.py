from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def students(request):
    students =['This is api project']
        
    
     
    return HttpResponse(students)
