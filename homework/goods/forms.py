from django import forms


class ImageForm(forms.Form):
    upload = forms.ImageField()
