import re

from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import Room, CustomUser, Comment, Address


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ["id", "name"]

    def validate_name(self, name):
        if not name:
            raise serializers.ValidationError("Name cannot be empty field")
        return name


class CustomUserSerializer(serializers.ModelSerializer):
    followed = serializers.SlugRelatedField(slug_field="login", queryset=CustomUser.objects.all(), many=True,
                                            default=[])

    class Meta:
        model = CustomUser
        fields = ["id", "login", "name", "surname", "email", "password", "followed", "is_active", "is_superuser"]

    def validate_name(self, name):
        if not name or not name.isalpha():
            raise serializers.ValidationError("Name cannot be empty field")
        return name.title()

    def validate_surname(self, surname):
        if not surname or not surname.isalpha():
            raise serializers.ValidationError("Surname cannot be empty field")
        return surname.title()

    def validate_login(self, login):
        if not login or not login.isalpha():
            raise serializers.ValidationError("Login cannot be empty field")
        return login

    def validate_email(self, email):
        regex = "^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"
        if not (re.search(regex, email)):
            raise serializers.ValidationError("Wrong email format!")
        else:
            return email

    def validate_password(self, password):
        if len(password) < 8:
            raise serializers.ValidationError(
                "Make sure your password is at lest 8 letters"
            )
        elif re.search("[0-9]", password) is None:
            raise serializers.ValidationError(
                "Make sure your password has a number in it"
            )
        elif re.search("[A-Z]", password) is None:
            raise serializers.ValidationError(
                "Make sure your password has a capital letter in it"
            )
        else:
            return make_password(password)


class CommentSerializer(serializers.ModelSerializer):
    room = serializers.SlugRelatedField(slug_field="name", queryset=Room.objects.all())
    user = serializers.SlugRelatedField(
        slug_field="login", queryset=CustomUser.objects.all()
    )

    class Meta:
        model = Comment
        fields = ["content", "room", "user"]

    def validate_content(self, content):
        if not content:
            raise serializers.ValidationError("You must type something!")
        elif len(content) > 254:
            raise serializers.ValidationError("Your comment can only have 254 letters!")
        else:
            return content


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ["country", "city", "street"]
