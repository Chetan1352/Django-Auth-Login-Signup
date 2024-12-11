from django.db import models

# Create your models here.
class Student(models.Model):
    # id=models.AutoField()
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    email=models.EmailField()
    address=models.TextField(null=True,blank=True)
   

class Car(models.Model):
    car_name=models.CharField(max_length=100)
    speed=models.IntegerField(default=40)

    def __str__(self) -> str:
        return self.car_name