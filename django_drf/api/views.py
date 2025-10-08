from rest_framework.response import Response
from students.models import Student
# Create your views here.
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET','POST'])
def studentsView(request):
    if request.method == 'GET': # get all the data from student table
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)# status code 200 ok

    elif request.method == 'POST': # create a new student
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    