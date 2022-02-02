from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    grade = models.FloatField()
    major = models.CharField(max_length=50)

    def __str__(self):
        return self.name
