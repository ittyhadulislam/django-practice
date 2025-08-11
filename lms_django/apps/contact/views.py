from django.shortcuts import render, redirect
from . form import ContactForm
# from django.http import HttpResponseRedirect

# Create your views here.
def contactForm(request):
    if request.method == "POST":
        form = ContactForm(request.POST, auto_id="contact_%s") #initial={"email" : "example@gmail.com"}
        if form.is_valid():
            print("First Name : ", form.cleaned_data["first_name"])
            return redirect("success")
        else:
            print("error")
            
    else:
        form = ContactForm()
    return render(request, "contact/contact.html", {"form": form})

def success(request):
    return render(request, "contact/success.html")