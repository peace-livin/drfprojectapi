from django.db import models

# Create your models here.


class Employee(models.Model):
    emp_id = models.CharField(primary_key=True)
    emp_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)


    def __str__(self):
        return self.emp_name