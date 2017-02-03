from django import forms
from center.models import Uploads


class UploadsForm(forms.ModelForm):
    class Meta:
        model = Uploads
        fields = ('relation','key','file','upload_file','fayl_name')