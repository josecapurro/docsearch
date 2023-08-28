from django import forms

class UploadFileForm(forms.Form):
    key = forms.CharField(max_length=130)
    file = forms.FileField()
