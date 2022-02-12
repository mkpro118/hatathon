from django.db import models

# Create your models here.


class Events(models.Model):
    title = models.CharField(max_length=200, blank=False, unique=True)
    date = models.DateField()
    location = models.CharField(max_length=300, blank=False, unique=False)
    attendance_count = models.IntegerField(blank=False)
    description = models.CharField(max_length=500, blank=False)
    cost = models.IntegerField(blank=True)
    capacity = models.IntegerField(blank=True)

    def __str__(self):
        return f'{self.title} - {self.description}'
