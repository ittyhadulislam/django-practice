from django.shortcuts import render
from . form import ContactForm
# Create your views here.
def contactForm(request):
    form = ContactForm(auto_id="contact_%s")
    return render(request, "contact/contact.html", {"form": form})