from django.http import JsonResponse

# Create your views here.


def studentsView(request):
    students={
        'id':1,
        'name':'akshay',
        'class':'IT'
    }
    return JsonResponse(students)