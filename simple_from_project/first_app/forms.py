from django import forms

class ProfileForm(forms.Form):
    name = forms.CharField(label="Your name")
    