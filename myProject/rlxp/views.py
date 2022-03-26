from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home_view(request):
  if request.user.is_authenticated:
    loggedIn = True
  else:
    loggedIn = False

  context = {
    "loggedIn": loggedIn,
    "username": request.user,
  }
  return render(request, 'rlxp/home.html', context)


#profile page
def profile_view(request):
  if request.user.is_authenticated:
    loggedIn = True
  else:
    loggedIn = False

  context = {
    "loggedIn": loggedIn,
    "username": request.user
  }
  return render(request, 'rlxp/profile.html', context)


def register_view(request):
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      raw_password = form.cleaned_data.get('password1')
      user = authenticate(username=username, password=raw_password)
      login(request, user)
      return redirect('home')
  else:
    form = UserCreationForm()
  return render(request, 'registration/register.html', {'form': form})
