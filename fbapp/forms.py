from django import forms
from .models import AppModel

textwidget = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))

class addform(forms.ModelForm):
    name = textwidget
    description = textwidget
    placeholder = textwidget
    randoms = forms.CharField(widget=forms.Textarea(attrs={'class':'textarea','rows':5}))
    cover = textwidget
    class Meta:
        model=AppModel
        exclude = ['user']