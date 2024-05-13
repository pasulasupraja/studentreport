from django.db import models


class Student(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='images')
    phone_number=models.IntegerField(max_length=10,blank=True)
    marks=models.CharField(max_length=100,blank=True)
    result=models.CharField(max_length=100)
    def __str__(self):
        return self.first_name