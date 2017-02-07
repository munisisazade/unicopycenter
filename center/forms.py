from django import forms
from center.models import Uploads


class UploadsForm(forms.ModelForm):
    class Meta:
        model = Uploads
        fields = ('relation','key','file')


class UploadFileForm(forms.Form):
    full_name = forms.CharField(max_length=255)
    check_user = forms.CharField(max_length=255)
    papertype = forms.CharField(max_length=255)
    listtype = forms.CharField(max_length=255)
