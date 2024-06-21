from django import forms
from .models import UploadedFile , Folder
from django.forms import HiddenInput

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file']

class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name', 'parent']
        widgets = {
                'parent': HiddenInput(),
            }
        
        
    