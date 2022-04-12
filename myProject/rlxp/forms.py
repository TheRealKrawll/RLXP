from django import forms
from .models import Student, Class, Assignment, Chore

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        #fields = '__all__'
        fields = ['fname', 'lname', 'age', 'grade_level', 'profile_pic']

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        #fields = '__all__'
        fields = ['name', 'subject']

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        #fields = '__all__'
        fields = ['name', 'difficulty', 'due_date']

class ChoreForm(forms.ModelForm):
    class Meta:
        model = Chore
        #fields = '__all__'
        fields = ['name', 'difficulty', 'due_date', 'recurring']