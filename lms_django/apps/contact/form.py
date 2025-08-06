from django import forms

class ContactForm(forms.Form):
    customer_id = forms.CharField(widget=forms.TextInput(attrs={"placeholder" : "Enter CID"}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder" : "Enter First Name"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder" : "Enter Last Name"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder" : "Enter Email"}))
    message = forms.CharField(widget=forms.Textarea(attrs={"placeholder" : "Leave your message"}))
    