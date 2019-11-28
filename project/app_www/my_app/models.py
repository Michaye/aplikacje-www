from .managers import CustomUserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class Room(models.Model):
    name = models.CharField(unique=True, max_length=254, blank=True, null=False)

    def __str__(self):
        return self.name


class CustomUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=254, blank=True, null=True)
    surname = models.CharField(max_length=254, blank=True, null=True)
    login = models.CharField(unique=True, max_length=254, blank=True, null=False)
    email = models.EmailField(unique=True, blank=True, null=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

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
    room = models.ForeignKey(to=Room, on_delete=models.PROTECT, blank=False, null=False)
