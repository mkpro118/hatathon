from django.db import models
from django.utils import timezone
from users.models import NewUser

# Create your models here.


class Group(models.Model):
    group_name = models.CharField(max_length=60, unique=True, blank=False,)
    members = models.ManyToManyField(NewUser, blank=True)
    group_image = models.ImageField(default='default.jpg', upload_to='group_pics')

    def __str__(self):
        return f'{self.group_name}'


class Message(models.Model):
    author = models.ForeignKey(NewUser, null=False, on_delete=models.CASCADE)
    time = models.DateTimeField(default=timezone.now)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    msg_content = models.CharField(max_length=1000, blank=False, unique=False)

    def __str__(self):
        return f'{self.author}: {self.msg_content}'
