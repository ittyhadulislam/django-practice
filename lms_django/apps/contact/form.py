from django import forms

class ContactForm(forms.Form):
    customer_id = forms.CharField(widget=forms.TextInput(attrs={"placeholder" : "Enter CID"}), min_length=4, max_length=6)
    first_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder" : "Enter First Name"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder" : "Enter Last Name"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder" : "Enter Email"}))
    message = forms.CharField(widget=forms.Textarea(attrs={"placeholder" : "Leave your message", "rows" : 5, "cols" : 50 }), )
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder" : "Password"}), min_length=8, max_length=15)
    re_password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder" : "Confirm Password"}), min_length=8, max_length=15)
    # payment = forms.DecimalField(min_value=100, max_value=500, max_digits=3, decimal_places=2)
    django = forms.BooleanField()
    
    def cleans(self):
        clean_data = super().clean()
        pass_match = self.cleaned_data["password"]
        re_pass_match = self.cleaned_data["re_password"]
        
        if pass_match != re_pass_match:
            raise forms.ValidationError("Password Doesn't match")