from django.db import models

# Create your models here.


class Events(models.Model):
    title = models.CharField(max_length=200, blank=False, unique=True, default='')
    date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=300, blank=False, unique=False, default='')
    attendance_count = models.IntegerField(blank=False, default=1)
    description = models.CharField(max_length=500, blank=False, default='')
    cost = models.IntegerField(blank=True, default=0)
    capacity = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return f'{self.title} - {self.description}'
