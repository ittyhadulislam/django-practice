from django.contrib import admin
from . models import courses

# Register your models here.
class coursesClass(admin.ModelAdmin):
    list_display = (
        "course_id",
        "course_name",
        "course_description",
        "course_duration",
        "course_price"
    )
admin.site.register(courses, coursesClass)