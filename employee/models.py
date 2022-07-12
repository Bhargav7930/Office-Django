from django.db import models

# Create your models here.
class Deparment(models.Model):
    name = models.CharField(max_length=100)
    location  = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=100,null = False)
    last_name = models.CharField(max_length=100)
    dept = models.ForeignKey(Deparment,on_delete=models.CASCADE)
    role = models.ForeignKey(Role,on_delete=models.CASCADE)
    salary = models.CharField(max_length=10)
    bonus = models.CharField(max_length=10)
    phone = models.CharField(max_length=12,null = False)
    hire_date = models.DateTimeField()

    def __str__(self)-> str:
        return "%s %s %s" %(self.first_name, self.last_name, self.phone)