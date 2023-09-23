from django import forms
from folder.models import File


class FileForm(forms.ModelForm):

    required_css_class = 'form-container'
    class Meta:
        model = File
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 500px;'}),  
        }


        def __init__(self, *args, **kwargs):
            super(FileForm, self).__init__(*args, **kwargs)
            self.fields['file'].widget.attrs.update({'class': 'form-control'})