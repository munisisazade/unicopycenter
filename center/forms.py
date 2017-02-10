from django import forms
from center.models import Uploads


class UploadsForm(forms.ModelForm):
    class Meta:
        model = Uploads
        fields = ('relation','key','file')


class UploadFileForm(forms.Form):
    full_name = forms.CharField(max_length=255)
    student = forms.CharField(max_length=255)
    universitet = forms.CharField(max_length=255,required=False)
    papertype = forms.CharField(max_length=255)
    listtype = forms.CharField(max_length=255)
    phone = forms.CharField(max_length=255)
