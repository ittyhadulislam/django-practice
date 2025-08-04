from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def course_list(request):
    return render(request, 'courses/course_list.html')
    # return HttpResponse('courses/course_list.html')