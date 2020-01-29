"""app_www URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from my_app.views import (
    Index,
    Users,
    Comments,
    Rooms,
    CreateUser,
    CreateRoom,
    AddComment,
    EditProfile,
    EditRoom,
    CreateUserAddress,
    BanUser,
    GetToken,
    FollowUser,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("rest_framework.urls")),
    path("", Index.as_view(), name="index"),
    path("users/", Users.as_view(), name="users"),
    path("rooms/", Rooms.as_view(), name="rooms"),
    path("comments/", Comments.as_view(), name="comments"),
    path("users/add/", CreateUser.as_view(), name="new_user"),
    path("rooms/add/", CreateRoom.as_view(), name="new_room"),
    path("comments/add/", AddComment.as_view(), name="new_comment"),
    path("users/edit/", EditProfile.as_view(), name="edit_profile"),
    path("rooms/edit/", EditRoom.as_view(), name="edit_room"),
    path("users/edit/address/", CreateUserAddress.as_view(), name="address"),
    path("ban/user=<int:id>/", BanUser.as_view(), name="ban"),
    path("users/follow/", FollowUser.as_view(), name="follow"),
    path("users/token/", GetToken.as_view(), name="token"),
]
