from django.shortcuts import render
from . form import ContactForm
# Create your views here.
def contactForm(request):
    if request.method == "POST":
        form = ContactForm(request.POST, auto_id="contact_%s") #initial={"email" : "example@gmail.com"}
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = ContactForm()
    return render(request, "contact/contact.html", {"form": form})