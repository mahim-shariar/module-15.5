from django import forms
from .models import muisician

class MusicianForm(forms.ModelForm):
    class Meta:
        model = muisician
        fields = '__all__'