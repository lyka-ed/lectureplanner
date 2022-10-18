from django.db import models

from datetime import time 

# Create your models here.

class Lab(models.Model):
    name = models.CharField(max_length=100)
    floor = models.IntegerField()
    lab_number = models.IntegerField()

    def __str__(self):
        return f"{self.name}: lab {self.lab_number} on floor {self.floor}"



class Lecture(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateField()
    time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)

    lab =  models.ForeignKey(Lab, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} at {self.time} on {self.date}"


