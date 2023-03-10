from django.contrib import admin
from profile_app import models

class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "profile_name",
        "cpf",
        "email"
    )

admin.site.register(models.User, UserAdmin)