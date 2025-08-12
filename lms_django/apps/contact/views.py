from django.shortcuts import render, redirect
from .form import ContactForm
from .models import ContactInfo


# Create your views here.
def contactForm(request):
    if request.method == "POST":
        form = ContactForm(
            request.POST, auto_id="contact_%s"
        )  # initial={"email" : "example@gmail.com"}
        if form.is_valid():
            cId = form.cleaned_data["customer_id"]
            firstName = form.cleaned_data["first_name"]
            lastName = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            django = form.cleaned_data["django"]
            password = form.cleaned_data["password"]
            rePassword = form.cleaned_data["re_password"]
            contact = ContactInfo(
                c_id=cId,
                first_name=firstName,
                last_name=lastName,
                email=email,
                message=message,
                is_django=django,
                password=password,
                re_password=rePassword,
            )
            contact.save()
            return redirect("success")
        else:
            print("error")

    else:
        form = ContactForm()
    return render(request, "contact/contact.html", {"form": form})


def success(request):
    return render(request, "contact/success.html")
