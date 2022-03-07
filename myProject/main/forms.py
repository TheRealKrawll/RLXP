from django import forms
from .models import Duck

class DuckForm(forms.ModelForm):
    class Meta:
        model = Duck
        fields = '__all__'

