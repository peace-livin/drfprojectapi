from rest_framework.response import Response
from students.models import Student
# Create your views here.
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET'])
def studentsView(request):
    if request.method == 'GET': # get all the data from student table
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)# status code 200 ok

    