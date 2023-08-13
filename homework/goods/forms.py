from django import forms


class FileForm(forms.Form):
    upload = forms.FileField()
