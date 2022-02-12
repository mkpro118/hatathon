from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (AbstractBaseUser,
                                        PermissionsMixin,
                                        BaseUserManager)
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
# Create your models here.


class NewAccountManager(BaseUserManager):
    def create_user(self, username, email, password, **other_fields):
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        return self.create_user(username, email, password, **other_fields)


class NewUser(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=200, blank=False, unique=True)
    email = models.EmailField(max_length=200, blank=False, unique=True)
    date_joined = models.DateField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = NewAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    @staticmethod
    def is_username_taken(username_to_check):
        users = NewUser.objects.all()
        for user in users:
            if user.username == username_to_check:
                return True
        else:
            return False

    @staticmethod
    def is_email_taken(email_to_check):
        users = NewUser.objects.all()
        for user in users:
            if user.email == email_to_check:
                return True
        else:
            return False


class Profile(models.Model):
    username = models.OneToOneField(NewUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default='anonymous', blank=True, unique=False)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return f'{self.username}'

    @receiver(post_save, sender=NewUser)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(username=instance)

    @receiver(post_save, sender=NewUser)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
