from django.contrib import admin
from .models import ContactInfo

# Register your models here.


class contactInfoClass(admin.ModelAdmin):
    list_display = (
        "c_id",
        "first_name",
        "last_name",
        "email",
        # "message",
        "password",
        "re_password",
        "is_django",
    )


admin.site.register(ContactInfo, contactInfoClass)
