from .managers import CustomUserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class Room(models.Model):
    room_type = models.CharField(unique=True, max_length=254, blank=True, null=True)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=254, blank=False, null=False)
    surname = models.CharField(max_length=254, blank=False, null=False)
    login = models.CharField(unique=True, max_length=254, blank=False, null=False)
    email = models.EmailField(blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField()

    USERNAME_FIELD = "login"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.login


class Comment(models.Model):
    content = models.CharField(max_length=254, blank=True, null=True)
    user = models.ForeignKey(
        to=CustomUser, on_delete=models.PROTECT, blank=False, null=False
    )
    room = models.ForeignKey(
        to=Room, on_delete=models.PROTECT, blank=False, null=False
    )
