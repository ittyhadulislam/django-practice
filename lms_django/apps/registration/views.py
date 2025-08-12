from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def registration(request):
    if request.method == "POST":
        reg_form = UserCreationForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
        else:
            print(reg_form.errors)
    else:
        reg_form = UserCreationForm()
    return render(request, "registration/registration.html", {"regForm": reg_form})