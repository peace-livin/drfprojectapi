from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('employees',views.EmployeesViewSet,basename='employees')

urlpatterns = [
    path('students/',views.studentsView,name='students'),
    path ('students/<int:pk>/',views.studentsDetailView),
   # path('employees/',views.Employees.as_view()),
   # path('employees/<str:pk>/',views.employeesDetail.as_view()),
    path('',include(router.urls)),
    path('blogs/',views.BlogsView.as_view()),
    path('comments/',views.CommentsView.as_view()),

    path('blogs/<int:pk>/',views.BlogsDetailView.as_view()),
    path('comments/<int:pk>/',views.CommentsDetailView.as_view()),
    ]
