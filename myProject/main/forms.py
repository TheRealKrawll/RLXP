from multiprocessing.context import DefaultContext
from django import forms

class NameForm(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20, )
    email = forms.EmailField(widget=forms.EmailInput)
    date = forms.DateField(widget=forms.SelectDateWidget)
    file = forms.ImageField(label="Enter an image")
