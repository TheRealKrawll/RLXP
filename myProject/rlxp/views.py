from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .forms import StudentForm, AssignmentForm, ChoreForm
from .models import Student, Assignment, Chore

# Create your views here.
def home_view(request):
  context = {
    "loggedIn": request.user.is_authenticated,
    "username": request.user,
  }
  return render(request, 'rlxp/home.html', context)


#profile page
def profile_view(request):
  context = {
    "loggedIn": request.user.is_authenticated,
    "username": request.user,
    "friends": {},
  }
  return render(request, 'rlxp/profile.html', context)

#dashboard page
def dashboard_view(request):
  student = Student.objects.get(user=request.user)
  chore = Chore(user=request.user)
  assignment = Assignment(user=request.user)
  choreForm = ChoreForm()
  assignmentForm = AssignmentForm()
  if request.method == "POST":
    #print("trying to post")
    if 'recurring' in request.POST:
      #print("chore")
      choreForm = ChoreForm(request.POST, instance=chore)
      if choreForm.is_valid():
        choreForm.save()
      else:
        print("form not valid")
    else:
      #print("recurring")
      assignmentForm = AssignmentForm(request.POST, instance=assignment)
      if assignmentForm.is_valid():
        assignmentForm.save()
    

  assignments = Assignment.objects.filter(user=request.user)
  chores = Chore.objects.filter(user=request.user)
  context = {
    "loggedIn": request.user.is_authenticated,
    "username": request.user,
    "student": student,
    "friends": {},
    "assignments": assignments,
    "chores": chores,
    "choreForm": choreForm,
    "assignmentForm": assignmentForm
  }
  return render(request, 'rlxp/dashboard.html', context)

def deleteAssignment(request, pk):
  Assignment.objects.filter(id=pk).delete()
  return redirect('dashboard')

def deleteChore(request, pk):
  Chore.objects.filter(id=pk).delete()
  return redirect('dashboard')



def register_view(request):
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      raw_password = form.cleaned_data.get('password1')
      user = authenticate(username=username, password=raw_password)
      login(request, user)

      #create Student object!!
      student = Student(user=request.user)
      student.save()
      return redirect('home')
  else:
    form = UserCreationForm()
  return render(request, 'registration/register.html', {'form': form})


def studentform_view(request):
  student = Student.objects.get(user=request.user)
  form = StudentForm(instance=student)
  if request.method == "POST":
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
      form.save()
      return redirect('profile')  

  context = {
    'form': form,
    "loggedIn": request.user.is_authenticated,
    "username": request.user
  }

  return render(request, 'rlxp/studentform.html', context)


