from django import forms
from .models import Duck, Room

class DuckForm(forms.ModelForm):
    class Meta:
        model = Duck
        fields = '__all__'

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        #fields = ['name', ...]

