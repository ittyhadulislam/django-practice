from django.shortcuts import render
from courses.models import courses
# Create your views here.
def home(request):
    course_details = courses.objects.all()[:4]
    return render(request, 'home_app/index.html', {"courses_details": course_details})