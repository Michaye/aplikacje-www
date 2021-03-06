from .managers import CustomUserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class Room(models.Model):
    name = models.CharField(unique=True, max_length=254, blank=False, null=False)

    def __str__(self):
        return self.name


class Address(models.Model):
    country = models.CharField(max_length=254, blank=True, null=True)
    city = models.CharField(max_length=254, blank=True, null=True)
    street = models.CharField(max_length=254, blank=True, null=True)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=254, blank=True, null=True)
    surname = models.CharField(max_length=254, blank=True, null=True)
    login = models.CharField(unique=True, max_length=254, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    address = models.ForeignKey(
        to=Address, on_delete=models.CASCADE, blank=True, null=True
    )
    followed = models.ManyToManyField(to='CustomUser', blank=True)

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
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    room = models.ForeignKey(to=Room, on_delete=models.PROTECT, blank=False, null=False)
