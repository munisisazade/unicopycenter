from django import forms
from center.models import Uploads


class UploadsForm(forms.ModelForm):
    class Meta:
        model = Uploads
        fields = ('relation','key','file','upload_file','fayl_name')


class UploadFileForm(forms.Form):
    full_name = forms.CharField(max_length=255)
    check_user = forms.CharField(max_length=255)
    papertype = forms.CharField(max_length=255)
    listtype = forms.CharField(max_length=255)
    phone = forms.CharField(max_length=255)
    file = forms.FileField()