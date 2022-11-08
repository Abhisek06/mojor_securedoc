from django import forms
from .models import Document
from django.contrib.auth.models import User

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('title','description', 'document','visible')

    title = forms.CharField(max_length=100)
    description = forms.CharField(max_length=500)
    vislist = forms.CharField(max_length=500)
    document = forms.FileField()
    visible = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        
    )
