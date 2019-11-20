from django.contrib import admin

# Register your models here.
from my_app.models import CustomUser, Comment, Room


admin.site.register(CustomUser)
admin.site.register(Comment)
admin.site.register(Room)
