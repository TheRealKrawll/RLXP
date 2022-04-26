from django import forms
from .models import Student, Assignment, Chore
from django.utils.translation import gettext_lazy as _

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        #fields = '__all__'
        fields = ['fname', 'lname', 'age', 'grade_level', 'profile_pic']
        #fields = ['fname']


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        #fields = '__all__'
        fields = ('name', 'difficulty', 'due_date')
        widgets = {
            'due_date': forms.DateInput(),
        }
        labels = {
            'name': _('Name'),
            'difficulty': _('Difficulty Level'),
            'due_date': _('Due Date (MM/DD/YYYY)'),
        }
        

class ChoreForm(forms.ModelForm):
    class Meta:
        model = Chore
        #fields = '__all__'
        fields = ['name', 'difficulty', 'recurring', 'due_date']
        widgets = {
            'due_date': forms.DateInput(),
        }
        labels = {
            'name': _('Name'),
            'difficulty': _('Difficulty Level'),
            'due_date': _('Due Date (MM/DD/YYYY)'),
        }
