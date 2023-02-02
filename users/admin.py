from django.contrib import admin
from django.contrib.auth import get_user_model

user = get_user_model()

class userAdmin(admin.ModelAdmin):
    list_display = ("email", "is_staff", "first_name", "phone")

admin.site.register(user, userAdmin)
