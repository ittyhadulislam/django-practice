from django import forms

class ContactForm(forms.Form):
    customer_id = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea())
    